# Generated by Django 3.1.2 on 2020-10-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0018_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('image_cart', models.ImageField(upload_to='static/images')),
            ],
        ),
    ]
