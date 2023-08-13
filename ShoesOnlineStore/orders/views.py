from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .utils import add_product_to_session, session_cart, remove_product_from_session
from orders.serializer import RemoveCartItemsSerializer, CartItemSerializer, OrderItemsSerializer
from django.conf import settings
import requests
import json
# from django.db.models import Subquery, OuterRef
# from shoes.models import Product, Price
# from .cart import Cart, CART_SESSION_ID
# Create a new session


# ? sandbox merchant
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

autho = ""

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "نهایی کردن خرید شما"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8080/order/verify_payment/'


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


def request_payment(request):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Description": description,
        "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json',
               'content-length': str(len(data))}
    try:
        response = requests.post(
            ZP_API_REQUEST, data=data, headers=headers, timeout=10)

        if response.status_code == 200:
            response = response.json()
            global autho
            autho = str(response['Authority'])
            if response['Status'] == 100:
                return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']), 'authority': response['Authority']}
            else:
                return {'status': False, 'code': str(response['Status'])}
        return response

    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}


def verify_payment(request):
    global autho
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Authority": autho,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json',
               'content-length': str(len(data))}
    response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            return {'status': True, 'RefID': response['RefID']}
        else:
            return {'status': False, 'code': str(response['Status'])}
    return response
