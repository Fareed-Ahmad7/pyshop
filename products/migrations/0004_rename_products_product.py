# Generated by Django 4.0.3 on 2022-03-03 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_offer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
