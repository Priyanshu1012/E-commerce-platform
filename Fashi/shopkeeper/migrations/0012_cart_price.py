# Generated by Django 3.1.2 on 2020-10-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0011_auto_20201007_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
