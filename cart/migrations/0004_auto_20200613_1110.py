# Generated by Django 3.0.5 on 2020-06-13 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20200613_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='item_name',
            field=models.TextField(),
        ),
    ]