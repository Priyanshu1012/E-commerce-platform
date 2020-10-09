# Generated by Django 3.1.2 on 2020-10-07 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0010_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='active',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='payment_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='payment_type',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='image_cart',
            field=models.ImageField(default=1, upload_to='static/images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='name',
            field=models.CharField(default=4, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
