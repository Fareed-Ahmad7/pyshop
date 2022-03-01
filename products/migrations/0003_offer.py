# Generated by Django 4.0.3 on 2022-03-01 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_name_alter_products_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='VCA2142', max_length=50)),
                ('description', models.CharField(default='20% off on all products', max_length=100)),
                ('discount', models.FloatField(default='0.2')),
            ],
        ),
    ]