# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Manager', '0002_auto_20151122_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='seat1',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='table',
            name='seat2',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='table',
            name='seat3',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='table',
            name='seat4',
            field=models.IntegerField(blank=True, default=-1),
        ),
    ]
