from django.db import models
from django.utils.translation import gettext_lazy as _


class ROLE(models.IntegerChoices):
    USER = 0, _('User')
    CUSTOMER = 1, _('Customer')
    MANAGER = 2, _('Manager')
    STAFF = 3, _('Staff')
