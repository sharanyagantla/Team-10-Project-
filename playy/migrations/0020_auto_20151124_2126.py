# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0019_auto_20151124_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='team_1',
        ),
        migrations.RemoveField(
            model_name='team1',
            name='match_name',
        ),
        migrations.RemoveField(
            model_name='team2',
            name='match_name2',
        ),
        migrations.AddField(
            model_name='match',
            name='match_name2',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team1',
            name='team_1',
            field=models.ForeignKey(default=0, to='playy.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team2',
            name='team_2',
            field=models.ForeignKey(default=0, to='playy.Team'),
            preserve_default=False,
        ),
    ]
