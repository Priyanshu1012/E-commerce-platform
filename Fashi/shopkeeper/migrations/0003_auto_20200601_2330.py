# Generated by Django 3.0.6 on 2020-06-01 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0002_auto_20200601_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
