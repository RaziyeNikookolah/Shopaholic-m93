from django.db.models.signals import post_save
from core.utils import PROVINCES
from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.validators import PhoneValidator
from shoes.models import Product
from .managers import AccountManager, CustomerManager
from core.utils import ROLE


class Account(BaseModel, AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name_plural = _("Accounts")
        verbose_name = _("Account")

    phone_validator = PhoneValidator()

    phone_number = models.CharField(
        _("phone number"),
        max_length=14,
        unique=True,
        help_text=(
            _("Required. 11 character. digits only.")
        ),
        validators=[phone_validator],
        error_messages={
            "unique": _("A user with that phone number already exists."),
        },
    )

    role = models.PositiveSmallIntegerField(_('role'),
                                            choices=ROLE.choices, default=ROLE.USER)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = AccountManager()

    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    def __str__(self) -> str:
        return f"User with phone number:{self.phone_number}"


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
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    gender = models.PositiveSmallIntegerField(
        _('gender'), choices=GENDER.choices, default=GENDER.FEMALE)
    birthday = models.DateField(_('birthday'), null=True, blank=True)
    bio = models.TextField(_('bio'), null=True, blank=True)
    image = models.ImageField(
        _('image'), upload_to=f'statics/profile/images/', default='statics/profile/images/profile.jpg', null=True, blank=True)
    email = models.EmailField(_('email'), null=True, blank=True)
    card_shaba_number = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self) -> str:
        return f'Profile for {self.first_name} {self.last_name}'

    def fullname(self):
        if self.first_name or self.last_name:
            return self.first_name+' '+self.last_name
        else:
            return 'Anonymous'


class Wishes(BaseModel):
    product_clicked_count = models.PositiveIntegerField(null=True, blank=True)
    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                related_name='wishes')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='wishes')


class Address(BaseModel):

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _('adresses')

    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='addresses', verbose_name=_("account"))
    province = models.CharField(
        max_length=7,
        choices=PROVINCES,
        verbose_name=_('Province'),
    )
    city = models.CharField(_("city"), max_length=40)
    address = models.TextField(_("adderess"), max_length=100)
    postal_code = models.CharField(_("postal code"), max_length=20)

    def __str__(self):
        return f'{self.province}, {self.city}, {self.address}'


def save_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(account=kwargs['instance'])


post_save.connect(save_profile, sender=Account)


class Customer(Account):
    objects = CustomerManager()

    class Meta:
        proxy = True
