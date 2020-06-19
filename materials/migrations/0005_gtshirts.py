# Generated by Django 3.0.5 on 2020-06-14 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_gpants'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gtshirts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_name', models.TextField()),
                ('size', models.TextField()),
                ('pcs', models.IntegerField()),
                ('image', models.ImageField(upload_to='pics')),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
                ('new', models.BooleanField(default=False)),
            ],
        ),
    ]
