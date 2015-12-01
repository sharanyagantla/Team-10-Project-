# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0052_auto_20151126_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='p1_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='p2_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='p3_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='p4_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='p5_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='userprofile',
            unique_together=set([('user', 'match')]),
        ),
    ]
