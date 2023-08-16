from django.conf import settings
import requests
import json


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
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8080/order/verify/'


def send_request(request):
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
            json_response = response.json()  # Store JSON response content
            if json_response['Status'] == 100:
                return {'status': True, 'url': ZP_API_STARTPAY + str(json_response['Authority']), 'authority': json_response['Authority']}
            else:
                return {'status': False, 'code': str(json_response['Status'])}
        # Return the response dictionary
        return {'status': False, 'response': response}

    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}


def verify(authority):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Authority": authority,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json',
               'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

        if response.status_code == 200:
            json_response = response.json()  # Store JSON response content
            if json_response['Status'] == 100:
                return {'status': True, 'RefID': json_response['RefID']}
            else:
                return {'status': False, 'code': str(json_response['Status'])}
        # Return the response dictionary
        return {'status': False, 'response': response}

    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}
