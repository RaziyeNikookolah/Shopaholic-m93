import logging
from orders.models import Order
from orders.models import Order
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from accounts import authentication
from .utils import add_product_to_session, session_cart, clear_session, create_orderItems_from_session
from orders.serializer import CartItemSerializer


logger = logging.getLogger('ShoesOnlineStore.orders')


class AddToCartView(APIView):
    permission_classes = (AllowAny,)

    @csrf_exempt
    def post(self, request, format=None):

        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data.get('product_id', '')
            quantity = serializer.validated_data.get('quantity', '')
            price = serializer.validated_data.get('price', '')
            total_price = serializer.validated_data.get('total_price', '')
            logger.info(f"order_id:{product_id} quantity:{quantity}")
            add_product_to_session(
                product_id, price, quantity, total_price)

            return Response({'message': 'item_added'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartListView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):

        session_data = session_cart()
        return Response(session_data)


class UpdateCartItemView(APIView):
    authentication_classes = []
    permission_classes = (AllowAny,)

    @csrf_exempt
    def post(self, request):
        if request.data:
            data = request.data  # Access the JSON data
            clear_session()
            for item in data.get('cart_items').values():
                add_product_to_session(
                    item['id'], item['price'], item['quantity'], item['sub_total'])
            return Response({'message': "Data received"}, status=status.HTTP_200_OK)
        else:
            return Response({'message': "Bad data"}, status=status.HTTP_400_BAD_REQUEST)


class CreateOrder(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [authentication.JWTAuthentication]

    @csrf_exempt
    def post(self, request):
        if request.data:
            data = request.data
            receiver_name = data.get('fname')
            receiver_last_name = data.get("lname")
            address = data.get("address")
            city = data.get("city")
            province = data.get("province")
            email = data.get("email")
            receiver_phone_number = data.get("phone_number")
            postal_code = data.get("postal_zip")
            note = data.get("order_note")
            user = request.user
            # user=Account.objects.filter(p)
            order_queryset = Order.objects.filter(
                account=user, is_paid=False).order_by('-create_timestamp')
            if not order_queryset.exists():
                order = Order.objects.create(account=user, receiver_name=receiver_name,
                                             receiver_lastname=receiver_last_name, address=address, city=city, province=province,
                                             email=email, postal_code=postal_code, note=note, receiver_phone_number=receiver_phone_number)
                order_instance = order_queryset.first()
            else:
                order_instance = order_queryset.first()

            create_orderItems_from_session(order_instance)
            total_price = order_instance.get_total_price()

            return Response({"order_id": order_instance.id, "total_price": total_price, 'message': "Order added successfully"}, status=status.HTTP_201_CREATED)

        return Response({'message': "Error"}, status=status.HTTP_400_BAD_REQUEST)


# class RemoveCartItemView(APIView):
#     permission_classes = (AllowAny,)

#     @csrf_exempt
#     def post(self, request):

#         serializer = RemoveCartItemsSerializer(data=request.data)
#         if serializer.is_valid():
#             product_id = serializer.validated_data.get('product_id', '')
#             return remove_product_from_session(product_id)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
