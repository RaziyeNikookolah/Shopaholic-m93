from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .utils import add_product_to_session, session_cart, remove_product_from_session
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
    print(111111)
    serializer = RemoveCartItemsSerializer(data=request.data)
    if serializer.is_valid():
        product_id = serializer.validated_data.get('product_id', '')
        print(22222)
        return remove_product_from_session(product_id)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def cart_list(request):
    session_whit_serialized_product = session_cart()
    return Response(session_whit_serialized_product)


@api_view(['POST'])
def order_create(request):
    ...
