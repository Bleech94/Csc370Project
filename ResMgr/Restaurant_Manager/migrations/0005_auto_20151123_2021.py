# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Manager', '0004_auto_20151123_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='seat1',
        ),
        migrations.RemoveField(
            model_name='table',
            name='seat2',
        ),
        migrations.RemoveField(
            model_name='table',
            name='seat3',
        ),
        migrations.RemoveField(
            model_name='table',
            name='seat4',
        ),
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.IntegerField(default=-1),
        ),
    ]
