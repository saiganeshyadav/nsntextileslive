# Generated by Django 3.0.5 on 2020-06-12 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartitems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('item_name', models.CharField(max_length=100)),
                ('item_image', models.ImageField(upload_to='pics')),
                ('item_price', models.IntegerField()),
            ],
        ),
    ]
