from django.contrib.auth.forms import UserCreationForm
from .models import Account


class UserCreationOrLoginForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("phone_number",)
