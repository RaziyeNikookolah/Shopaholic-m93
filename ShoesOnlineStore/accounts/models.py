from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from core.validators import PhoneValidator
from .managers import AccountManager


class Account(BaseModel, AbstractBaseUser):

    class Meta:
        verbose_name_plural = _("Accounts")
        verbose_name = _("Account")

    class Role(models.IntegerChoices):
        USER = 0, _('User')
        CUSTOMER = 1, _('Customer')
        PRODUCT_MANAGER = 2, _('Manager')
        OPERATOR = 3, _('Operator')

    phone_validator = PhoneValidator()

    phone_number = models.CharField(
        _("phone number"),
        max_length=11,
        unique=True,
        help_text=(
            _("Required. 11 character. digits only.")
        ),
        validators=[phone_validator],
        error_messages={
            "unique": _("A user with that phone number already exists."),
        },
    )

    role = models.PositiveSmallIntegerField(_('role'), max_length=10,
                                            choices=Role.choices, default=Role.USER)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = AccountManager()

    def __str__(self) -> str:
        return f"{self.phone_number}"

    def fullname(self):
        if self.first_name or self.last_name:
            return self.first_name+' '+self.last_name
        else:
            return 'Anonymous'
