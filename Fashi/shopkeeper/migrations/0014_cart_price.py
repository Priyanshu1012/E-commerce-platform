# Generated by Django 3.1.2 on 2020-10-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0013_remove_cart_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]