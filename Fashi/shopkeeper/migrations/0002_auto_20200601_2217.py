# Generated by Django 3.0.6 on 2020-06-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(upload_to='D:/Fashi/shopkeeper/static/images'),
        ),
    ]
