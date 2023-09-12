from django import forms


class UserRegiterOrLoginForm(forms.Form):
    phone_number = forms.CharField(max_length=14)
