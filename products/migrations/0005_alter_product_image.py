# Generated by Django 4.0 on 2021-12-28 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(default=None, max_length=10000),
        ),
    ]
