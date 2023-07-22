from django.contrib.auth.base_user import BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, phone_number, **extra_fields):

        if not phone_number:
            raise ValueError('The phone must be set')

        account = self.model(phone_number=phone_number, **extra_fields)

        return account

    def create_superuser(self, phone_number, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(phone_number, **extra_fields)
