# Generated by Django 4.0 on 2021-12-08 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='title',
        ),
    ]