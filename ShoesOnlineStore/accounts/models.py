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


class Profile(BaseModel):

    class GENDER(models.IntegerChoices):
        MALE = 1, _('Male')
        FEMALE = 2, _('Female')
        OTHER = 3, _('Other')

    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.PositiveSmallIntegerField(
        _('gender'), choices=GENDER.choices, null=True, blank=True, default=GENDER.FEMALE)
    birthday = models.DateField(_('birthday'), null=True, blank=True)
    bio = models.TextField(_('bio'), null=True, blank=True)
    image = models.ImageField(
        _('image'), upload_to=f'statics/profile/images/', default='statics/profile/images/profile.jpg', null=True, blank=True)
    email = models.EmailField(_('email'), null=True, blank=True)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self) -> str:
        return f'profile for {self.user}'
