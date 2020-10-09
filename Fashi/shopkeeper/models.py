from django.db import models

class Items(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/images')

# Create your models here.
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phonenumber = models.IntegerField()
    message = models.CharField(max_length=200)

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.FloatField()
    total_price = models.FloatField()
    image_cart = models.ImageField(upload_to='static/images')

