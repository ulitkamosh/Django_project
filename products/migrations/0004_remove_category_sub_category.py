# Generated by Django 3.0.5 on 2020-04-29 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_sub_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
    ]
