# Generated by Django 3.1.2 on 2020-10-08 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0014_cart_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
    ]