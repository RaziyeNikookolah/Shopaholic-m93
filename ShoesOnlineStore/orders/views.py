import csv
import logging


from orders.models import Order
from django.http import HttpResponse
from django.utils import timezone
from orders.models import Order, OrderItem
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from accounts import authentication
from .utils import add_product_to_session, session_cart, remove_product_from_session, clear_session, create_orderItems_from_session
from orders.serializer import RemoveCartItemsSerializer, CartItemSerializer, OrderItemsSerializer


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


class RemoveCartItemView(APIView):
    permission_classes = (AllowAny,)

    @csrf_exempt
    def post(self, request):

        serializer = RemoveCartItemsSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data.get('product_id', '')
            return remove_product_from_session(product_id)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartListView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):

        session_data = session_cart()
        return Response(session_data)


class OrderCreateView(APIView):
    def post(self, request, format=None):
        ...
        return Response("Order created successfully.")


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


class CheckoutView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        ...
        # if request.user:
        #     return Response({"message": "User is Logged in"}, status=status.HTTP_100_CONTINUE)
        # else:
        #     return Response({"message": "login required"}, status=status.HTTP_401_UNAUTHORIZED)


class CreateOrder(APIView):
    permission_classes = (AllowAny,)

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
            print(user)
            # user=Account.objects.filter(p)
            order = Order.objects.filter(
                account=user, is_paid=False).order_by('-create_timestamp')
            if not order.exists():
                order = Order.objects.create(account=user, receiver_name=receiver_name,
                                             receiver_lastname=receiver_last_name, address=address, city=city, province=province,
                                             email=email, postal_code=postal_code, note=note, receiver_phone_number=receiver_phone_number)
                order = Order.objects.filter(
                    account=user, is_paid=False).order_by('-create_timestamp').first()
            order = order.first()
            create_orderItems_from_session(order)
            # clear_session() not here it will be done when order paid
            total_price = order.get_total_price()
            return Response({"order_id": order.id, "total_price": total_price, 'message': "Order added successfully"}, status=status.HTTP_201_CREATED)

        return Response({'message': "Error"}, status=status.HTTP_400_BAD_REQUEST)


# def export(request):  # no one can not call this view use user_passes_test
#     response = HttpResponse(content_type='text/csv')
#     writer = csv.writer(response)
#     writer.writerow(['Products in order:'])
#     today = timezone.now().date()

#     orders_created_today = Order.objects.filter(create_timestamp__date=today).select_related('items').values(
#         'id', 'create_timestamp', 'is_paid', 'receiver_name', 'receiver_lastname', 'city')

#     for order in orders_created_today:
#         writer.writerow([order['create_timestamp'], order['is_paid'],
#                         order['receiver_name'], order['receiver_lastname'], order['city']])

#         items = OrderItem.objects.filter(order_id=order['id'])
#         for item in items:

#             writer.writerow([item.product, item.quantity, item.final_price])

#     response['Content-Disposition'] = 'attachment; filename="orders.csv"'

#     return response
