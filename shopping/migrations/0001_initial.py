# Generated by Django 5.0.6 on 2024-07-06 01:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='商品名')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='価格(円)')),
            ],
        ),
    ]
