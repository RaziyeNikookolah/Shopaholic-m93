from django.shortcuts import redirect
from django.http import HttpResponse
import json
from django.conf import settings
from django.views import View
import requests
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from accounts import authentication
from .utils import add_product_to_session, session_cart, remove_product_from_session, clear_session
from orders.serializer import RemoveCartItemsSerializer, CartItemSerializer, OrderItemsSerializer


# ZP_API_REQUEST = "https://sandbox.zarinpal.com/pg/v4/payment/request.json"
# ZP_API_VERIFY = "https://sandbox.zarinpal.com/pg/v4/payment/verify.json"
# ZP_API_STARTPAY = "https://sandbox.zarinpal.com/pg/StartPay/"

# amount = 1000  # Rial / Required
# description = "نهایی کردن خرید شما"  # Required
# # phone = 'YOUR_PHONE_NUMBER'  # Optional
# # Important: need to edit for realy server.
# CallbackURL = 'http://127.0.0.1:8080/order/verify_payment/'


# class ZarrinPalRequestPayment(View):
#     # authentication_classes = []
#     # permission_classes = (AllowAny,)

#     def get(self, request):
#         data = {
#             "MerchantID": settings.MERCHANT,
#             "Amount": 1000,
#             "Description": "Finalize your order",
#             # "Phone": phone,
#             "CallbackURL": 'http://127.0.0.1:8080/order/verify_payment/'
#             # 'http://127.0.0.1:8000/thank_you/',
#         }
#         data = json.dumps(data)
#         # set content length by data
#         headers = {"accept": "application/json", 'content-type': 'application/json',
#                    #    'content-length': str(len(data))
#                    }

#         req = requests.post(
#             ZP_API_REQUEST, data=data, headers=headers, timeout=10)

#         # authority = req.json()['data']['authority']
#         # if len(req.json()['errors']) == 0:
#         return redirect(ZP_API_STARTPAY.format(authority=autho))
#         # else:
#         # e_code = req.json()['errors']['code']
#         # e_message = req.json()['errors']['message']
#         # f"Error code: {e_code}, Error Message: {e_message}")
#         # return HttpResponse("error")


# class ZarrinPalVerifyPayment(View):
#     # authentication_classes = []
#     # permission_classes = (AllowAny,)

#     def get(self, request):
#         global autho
#         data = {
#             "MerchantID": settings.MERCHANT,
#             "Amount": amount,
#             "Authority": autho,
#         }
#         data = json.dumps(data)
#         # set content length by data
#         headers = {'content-type': 'application/json',
#                    'content-length': str(len(data))}
#         response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

#         if response.status_code == 200:
#             response = response.json()
#             if response['Status'] == 100:
#                 return {'status': True, 'RefID': response['RefID']}
#             else:
#                 return {'status': False, 'code': str(response['Status'])}
#         return response


class AddToCartView(APIView):
    authentication_classes = []
    permission_classes = (AllowAny,)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data.get('product_id', '')
            quantity = serializer.validated_data.get('quantity', '')
            price = serializer.validated_data.get('price', '')
            total_price = serializer.validated_data.get('total_price', '')
            add_product_to_session(product_id, price, quantity, total_price)

            return Response({'message': 'item_added'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveCartItemView(APIView):
    authentication_classes = []
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
    authentication_classes = []
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        session_with_serialized_product = session_cart()
        return Response(session_with_serialized_product)


class OrderCreateView(APIView):
    def post(self, request, format=None):
        # Your logic for order creation here
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
    authentication_classes = [authentication.LoginAuthentication]

    def get(self, request):
        ...
        # if request.user:
        #     return Response({"message": "User is Logged in"}, status=status.HTTP_100_CONTINUE)
        # else:
        #     return Response({"message": "login required"}, status=status.HTTP_401_UNAUTHORIZED)
