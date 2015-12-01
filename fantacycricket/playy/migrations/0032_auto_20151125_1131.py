# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0031_auto_20151125_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='player1_points',
        ),
        migrations.RemoveField(
            model_name='match',
            name='player2_points',
        ),
        migrations.RemoveField(
            model_name='match',
            name='player3_points',
        ),
        migrations.RemoveField(
            model_name='match',
            name='player4_points',
        ),
        migrations.RemoveField(
            model_name='match',
            name='player_1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='player_2',
        ),
        migrations.RemoveField(
            model_name='match',
            name='player_3',
        ),
        migrations.RemoveField(
            model_name='match',
            name='player_4',
        ),
        migrations.AddField(
            model_name='player',
            name='match',
            field=models.ForeignKey(default=0, to='playy.Match'),
            preserve_default=False,
        ),
    ]
