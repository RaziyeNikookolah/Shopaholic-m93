from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _



@deconstructible
class PhoneValidator(validators.RegexValidator):
    regex = r'(09)([0-9]{9})|(\+989)([0-9]{9})'
    message = _(
        "Enter a valid phone. Your Phone Number should be 11 number and start with 09 or +98"
    )
    flags = 0
