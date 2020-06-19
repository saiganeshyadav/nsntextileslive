from django.db import models

# Create your models here.

class Gshirts(models.Model):
    Item_name = models.TextField()
    size = models.TextField()
    pcs = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    new = models.BooleanField(default=False)

class Gpants(models.Model):
    Item_name = models.TextField()
    size = models.TextField()
    pcs = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    new = models.BooleanField(default=False)

class Gtshirts(models.Model):
    Item_name = models.TextField()
    size = models.TextField()
    pcs = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    new = models.BooleanField(default=False)

class Kshirts(models.Model):
    Item_name = models.TextField()
    size = models.TextField()
    pcs = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    new = models.BooleanField(default=False)


class Kpants(models.Model):
    Item_name = models.TextField()
    size = models.TextField()
    pcs = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    new = models.BooleanField(default=False)


class Kshirtspants(models.Model):
    Item_name = models.TextField()
    size = models.TextField()
    pcs = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    new = models.BooleanField(default=False)


class Sherwani(models.Model):
    Item_name = models.TextField()
    size = models.TextField()
    pcs = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    new = models.BooleanField(default=False)

class Ksuits(models.Model):
    Item_name = models.TextField()
    size = models.TextField()
    pcs = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    new = models.BooleanField(default=False)


class Kdothi(models.Model):
    Item_name = models.TextField()
    size = models.TextField()
    pcs = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    new = models.BooleanField(default=False)


class Lleggins(models.Model):
    Item_name = models.TextField()
    size = models.TextField()
    pcs = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    new = models.BooleanField(default=False)


class Ldresses(models.Model):
    Item_name = models.TextField()
    size = models.TextField()
    pcs = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    new = models.BooleanField(default=False)