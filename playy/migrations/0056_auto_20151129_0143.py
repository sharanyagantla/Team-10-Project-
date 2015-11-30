# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0055_auto_20151128_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='p1_points',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='p2_points',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='p3_points',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='p4_points',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='p5_points',
        ),
    ]
