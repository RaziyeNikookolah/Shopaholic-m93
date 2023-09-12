from django.db import models
from datetime import datetime, timedelta, timezone
import random
import string
from django.utils.translation import gettext_lazy as _


class OtpRequest(models.Model):
    create_timestamp = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=14)
    code = models.CharField(max_length=4, null=True)
    valid_until = models.DateTimeField(
        default=datetime.now(timezone.utc)+timedelta(seconds=120))

    def is_expired(self):
        if self.valid_until < datetime.now(timezone.utc):
            return True
        return False

    class Meta:

        verbose_name = _("OneTimePassword")
        verbose_name_plural = _("OneTimePasswords")

    def generate_code(self):
        self.code = self._random_code()
        self.valid_until = datetime.now(timezone.utc) + timedelta(seconds=120)

    def _random_code(self):
        rand = random.SystemRandom()
        # it gives list of 4 char digit
        digits = rand.choices(string.digits, k=4)
        return ''.join(digits)
