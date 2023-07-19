from django.db import models
from core.models import BaseModel


class Customer(BaseModel):
    
    class Meta:
        verbose_name_plural = "Customers"
    
    class Gender(models.IntegerChoices):
        MALE = 0, "مرد 👨"
        FEMALE = 1, "زن "

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=14)
    gender = models.IntegerField(
        choices=Gender.choices, default=1)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    
class Address(BaseModel):
    class Meta:
        verbose_name_plural = "Addresses"
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    postal_code=models.CharField(max_length=10)
    details = models.TextField(max_length=500)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,related_name="addresses")
    def __str__(self) -> str:
        return f"{self.city} , {self.postal_code}"
    