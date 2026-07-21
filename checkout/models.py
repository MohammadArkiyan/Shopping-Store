from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name='FirstName')
    last_name = models.CharField(max_length=70, verbose_name='LastName')
    email = models.EmailField(max_length=200, verbose_name='Email')
    phone_number = models.CharField(max_length=12, verbose_name='PhoneNumber')
    address_line1 = models.TextField(verbose_name='AddressLine1')
    address_line2 = models.TextField(verbose_name='AddressLine2')
    postal_code = models.IntegerField(verbose_name='PostalCode')
    country = models.CharField(max_length=20, verbose_name='Country')
    city =models.CharField(max_length=40, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    is_billing = models.BooleanField(verbose_name='OriginAddress')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} form {self.country} {self.city}"


    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


