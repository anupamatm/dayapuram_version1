from email.policy import default
from django.db import models
from datetime import date
from reseller_app.models import Product


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=200,default="")

class AddCart(models.Model):
    product  = models.ForeignKey(Product, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    qty = models.IntegerField(default=1)

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    productid = models.ForeignKey(Product,on_delete=models.CASCADE)
    address = models.CharField(max_length=200, default="")
    quantity = models.IntegerField()
    status = models.CharField(max_length=20,default="") #update after payment confirmed
    date = models.DateField(default=date.today)
    


