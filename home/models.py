from django.db import models

# Create your models here.
class Items(models.Model):
    Item_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)