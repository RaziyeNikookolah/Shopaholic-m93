from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
import requests
import json

from orders.models import Order


# ? sandbox merchant
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'


ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8080/order/verify/'


class PaymentRequest(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        request.session["order_payment"] = {"order_id": order.id}
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": int(round(float(order.get_total_price()))),
            "Description": description,
            # "Phone": phone,
            "CallbackURL": CallbackURL,
        }
        data = json.dumps(data)
        # set content length by data
        headers = {
            'accept': 'application/json',
            'content-type': 'application/json',
            'content-length': str(len(data))}

        response = requests.post(
            ZP_API_REQUEST, data=data, headers=headers, timeout=10)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return redirect(ZP_API_STARTPAY + str(response['Authority']))
            elif response.get("errors"):
                error_code = response["errors"]["code"]
                error_message = response["errors"]["message"]
                return HttpResponse(f"Error code:{error_code},error message:{error_message}")
        return HttpResponse(response.items())


class PaymentVerify(View):
    def get(self, request):
        order_id = request.session['order_payment']["order_id"]
        order = Order.objects.get(id=int(order_id))
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": int(round(float(order.get_total_price()))),
            "Authority": request.GET["authority"],
        }
        data = json.dumps(data)
        # set content length by data
        headers = {
            'accept': "application/json",
            'content-type': 'application/json',
            'content-length': str(len(data))}
        response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100 or response['Status'] == 101:
                order.is_paid = True
                # order.transaction_id=response["RefID"]
                # delete session
                order.save()

                return HttpResponse(f"Transaction success RefID:{str(response['RefID'])} , Status:{response['status']}")
            else:

                return HttpResponse(f"Transaction failed Status:{response['status']}")
        return response
