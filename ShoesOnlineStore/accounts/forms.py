from django import forms


class UserCreationOrLoginForm(forms.Form):
    phone_number = forms.CharField(max_length=14)
