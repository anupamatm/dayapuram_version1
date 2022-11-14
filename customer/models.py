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

class Addresslist(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    selected_address = models.CharField(max_length=200)

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    productid = models.ForeignKey(Product,on_delete=models.CASCADE)
    address = models.ForeignKey(Addresslist,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20,default="placed") #update after payment confirmed
    

class Payment(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    total_amount = models.FloatField()
    date = models.DateField(default=date.today)
    p_status = models.CharField(max_length=20,default="fail")
    

class Order_details(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    address = models.ForeignKey(Addresslist,on_delete=models.CASCADE)


 



