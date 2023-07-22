from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import UserPassesTestMixin
from kavenegar import *


def send_otp_code(phone_number, code):
    try:
     # TODO env
        api = KavenegarAPI(
            '563470796A30362B74617A5167474C4A614F774970523458474632726E724E63343852434A34586C5A44593D')
        params = {
            'sender': '',  # if i pay money  I 'll get special phone_number
            'receptor': phone_number,
            'message': f'{code}  کد تایید شما '
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


class ROLE(models.IntegerChoices):
    USER = 0, _('User')
    CUSTOMER = 1, _('Customer')
    MANAGER = 2, _('Manager')
    STAFF = 3, _('Staff')

