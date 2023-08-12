from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .utils import add_product_to_session, session_cart, session, session_key
from orders.serializer import RemoveCartItemsSerializer, CartItemSerializer, OrderItemsSerializer
# from django.db.models import Subquery, OuterRef
# from shoes.models import Product, Price
# from .cart import Cart, CART_SESSION_ID
# Create a new session


@csrf_exempt
@api_view(['POST'])
def add_to_cart(request):

    serializer = CartItemSerializer(data=request.data)

    if serializer.is_valid():
        product_id = serializer.validated_data.get('product_id', '')
        quantity = serializer.validated_data.get('quantity', '')
        price = serializer.validated_data.get('price', '')
        total_price = serializer.validated_data.get('total_price', '')
        add_product_to_session(product_id,
                               price, quantity, total_price)

        return Response({'message': 'item_added'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def remove_from_cart(request):
    serializer = RemoveCartItemsSerializer(data=request.data)
    product_id = serializer.validated_data.get('product_id', '')
    if serializer.is_valid():
        # cart.remove(product_id)
        global cart
        if product_id in cart:
            del cart[product_id]
            global session
            session.modified = True

        return Response({'message': 'cart item removed'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def cart_list(request):
    session_whit_serialized_product = session_cart()
    # for k, v in session_whit_serialized_product:
    #     print("************")
    #     print(k, v)

    # serializer = OrderItemsSerializer(
    #     session_whit_serialized_product, many=True)
    # serialized_data = serializer.data
    return Response(session_whit_serialized_product)
# @api_view(['GET'])
# def cart_list(request):
#     global session
#     session_with_serialized_product = session_cart(session)

#     # Serialize each item in the cart separately
#     serialized_items = []
#     for item in session_with_serialized_product['cart_items']:
#         serialized_item = OrderItemsSerializer(data=item)
#         if serialized_item.is_valid():
#             serialized_items.append(serialized_item)
#         else:
#             # Handle any invalid data, such as skipping or logging an error
#             # For simplicity, let's skip the invalid item here
#             continue

#     # Convert the list of serialized items to JSON-serializable data
#     serialized_data = [item.data for item in serialized_items]

#     return Response(serialized_data)
