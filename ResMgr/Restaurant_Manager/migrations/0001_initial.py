# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('name', models.CharField(primary_key=True, serialize=False, max_length=30)),
                ('customer_price', models.FloatField()),
                ('ingredient_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_type', models.CharField(primary_key=True, serialize=False, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('phone_number', models.CharField(serialize=False, max_length=16)),
                ('address', models.CharField(primary_key=True, max_length=40)),
                ('postal_code', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('occupied', models.BooleanField()),
            ],
        ),
    ]
