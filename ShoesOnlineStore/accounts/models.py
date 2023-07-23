from datetime import timedelta
import random
import string
from uuid import uuid4
from django.utils import timezone
from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.validators import PhoneValidator
from .managers import AccountManager
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
        return f'Profile for {self.user}'


class Address(BaseModel):

    PROVINCES = [
        ('thr', _('Tehran')),
        ('az-sh', _('Azarbayejan Sharghi')),
        ('az-gh', _('Azarbayejan Gharbi')),
        ('ard', _('Ardebil')),
        ('esf', _('Esfehan')),
        ('alb', _('Alborz')),
        ('ilm', _('Ilam')),
        ('bsh', _('Booshehr')),
        ('chm', _('Charmahal o Bakhtiari')),
        ('kh-j', _('Khorasan Jonobi')),
        ('kh-r', _('Khorasan Razavi')),
        ('kh-sh', _('Khorasan Shomali')),
        ('khz', _('Khoozestan')),
        ('znj', _('Zanjan')),
        ('smn', _('Semnan')),
        ('sbch', _('Sistan Baloochestan')),
        ('frs', _('Fars')),
        ('ghz', _('Ghazvin')),
        ('qom', _('Qom')),
        ('krd', _('Kordestan')),
        ('krm', _('Kerman')),
        ('kr-sh', _('Kerman Shah')),
        ('khb', _('Kohkilooye Boyer Ahmad')),
        ('gls', _('Golestan')),
        ('gil', _('Gilan')),
        ('lor', _('Lorestan')),
        ('maz', _('Mazandaran')),
        ('mrk', _('Markazi')),
        ('hrm', _('Hormozgan')),
        ('hmd', _('Hamedan')),
        ('yzd', _('Yazd')),
    ]

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
    # receiver=# etelaate khodesh ya ye nafar dige

    def __str__(self):
        return f'{self.country}, {self.province}, {self.city}, {self.address}'


class OtpRequest(models.Model):
    request_id = models.UUIDField(default=uuid4, editable=False)
    phone_number = models.CharField(max_length=14)
    code = models.CharField(max_length=4, null=True)
    valid_from = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(
        default=timezone.now()+timedelta(seconds=120))
    # the response of otp service
    receipt_id = models.CharField(max_length=255, null=True)

    class Meta:

        verbose_name = _("OneTimePassword")
        verbose_name_plural = _("OneTimePasswords")

    def generate_password(self):
        self.password = self._random_code()
        self.valid_until = timezone.now+timedelta(seconds=120)

    def _random_code(self):
        rand = random.SystemRandom()
        # it gives list of 4 char digit
        digits = rand.choices(string.digits, k=4)
        return ''.join(digits)
