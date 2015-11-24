# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Manager', '0007_auto_20151124_1309'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='customer',
        ),
        migrations.AddField(
            model_name='receipt',
            name='table',
            field=models.IntegerField(default=-1),
        ),
    ]
