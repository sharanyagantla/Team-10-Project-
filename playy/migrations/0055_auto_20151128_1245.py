# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0054_userprofile_total_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='p1_points',
            field=models.ForeignKey(related_name='p1points', to='playy.AsignPoints'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='p2_points',
            field=models.ForeignKey(related_name='p2points', to='playy.AsignPoints'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='p3_points',
            field=models.ForeignKey(related_name='p3points', to='playy.AsignPoints'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='p4_points',
            field=models.ForeignKey(related_name='p4points', to='playy.AsignPoints'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='p5_points',
            field=models.ForeignKey(related_name='p5points', to='playy.AsignPoints'),
        ),
    ]
