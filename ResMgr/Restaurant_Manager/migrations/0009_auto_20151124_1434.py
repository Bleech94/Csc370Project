# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Manager', '0008_auto_20151124_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='customer_total',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='ingredient_total',
            field=models.FloatField(blank=True),
        ),
    ]
