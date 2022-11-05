from email.policy import default
from django.db import models

from reseller_app.models import Product


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=30)

class AddCart(models.Model):
    product  = models.ForeignKey(Product, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    qty = models.IntegerField(default=1)