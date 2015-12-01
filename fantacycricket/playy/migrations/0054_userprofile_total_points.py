# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0053_auto_20151128_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='total_points',
            field=models.IntegerField(default=0),
        ),
    ]
