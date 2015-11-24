# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Manager', '0003_auto_20151123_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
