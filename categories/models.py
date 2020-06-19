from django.db import models

# Create your models here.
class Gents(models.Model):
    Item_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Kids(models.Model):
    Item_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Suits(models.Model):
    Item_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Ladies(models.Model):
    Item_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)