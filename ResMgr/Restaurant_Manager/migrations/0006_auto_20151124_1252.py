# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Manager', '0005_auto_20151123_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('number', models.AutoField(serialize=False, primary_key=True)),
                ('customer', models.IntegerField(default=-1)),
                ('foodItem', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Receipts',
            fields=[
                ('number', models.AutoField(serialize=False, primary_key=True)),
                ('customer', models.IntegerField(default=-1)),
                ('customer_total', models.FloatField()),
                ('ingredient_total', models.FloatField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Order',
            new_name='Customers',
        ),
        migrations.RenameModel(
            old_name='FoodItem',
            new_name='FoodItems',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
