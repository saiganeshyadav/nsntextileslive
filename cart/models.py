from django.db import models

# Create your models here.

class Cartitems(models.Model):
    customer=models.TextField()
    item_name=models.TextField()
    item_image= models.ImageField(upload_to='pics')
    item_price=models.IntegerField()
    item_pcs=models.IntegerField()
    item_size=models.TextField()


class Order(models.Model):
    shop_name = models.TextField()
    adress = models.TextField()
    shop_email = models.TextField()
    shop_number = models.BigIntegerField()
    cust_name = models.TextField()
    ord_name = models.TextField()
    ord_img = models.ImageField(upload_to='pics')
    ord_size = models.TextField()
    ord_pcs = models.IntegerField()
    ord_price = models.IntegerField()


