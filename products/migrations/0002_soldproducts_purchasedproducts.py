# Generated by Django 4.0 on 2021-12-27 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, default='empty.jpg', null=True, upload_to='')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sold_products', to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='PurchasedProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, default='empty.jpg', null=True, upload_to='media')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchased_products', to='accounts.user')),
            ],
        ),
    ]
