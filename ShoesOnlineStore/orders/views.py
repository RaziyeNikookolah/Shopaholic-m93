from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from orders.serializer import AddCartItemsSerializer, RemoveCartItemsSerializer, CartItemSerializer
# from django.db.models import Subquery, OuterRef
# from shoes.models import Product, Price
# from .cart import Cart, CART_SESSION_ID
# Create a new session
session = SessionStore()


def add_product_to_session(session_key, id, price, quantity):
    global session
    if session_key not in session:
        session = SessionStore(session_key=session_key)

    if session_key not in session:
        session[session_key] = []

    product = {
        'id': id,
        'price': str(price),
        'quantity': quantity
    }
    for item in session[session_key]:
        if item['id'] == id:
            session[session_key].remove(item)
    session[session_key].append(product)
    session.save()

    return session.session_key


@csrf_exempt
@api_view(['POST'])
def add_to_cart(request):
    serializer = AddCartItemsSerializer(data=request.data)
    if serializer.is_valid():

        product_id = serializer.validated_data.get('product_id', '')
        quantity = serializer.validated_data.get('quantity', '')
        price = serializer.validated_data.get('price', '')

        add_product_to_session('products', product_id, price, quantity)

        # for item in session['products']:
        #     print(item)

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
    global cart
    for c in cart.items():
        print(c)

    serializer = CartItemSerializer(cart, many=True)
    serialized_data = serializer.data
    return Response(serialized_data)
