# Generated by Django 3.0.5 on 2020-04-29 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='additional_info',
        ),
    ]
