# Generated by Django 3.0.5 on 2020-06-11 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gshirts',
            name='new',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='gshirts',
            name='pcs',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gshirts',
            name='size',
            field=models.TextField(),
        ),
    ]