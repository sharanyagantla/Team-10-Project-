# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0021_auto_20151124_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team1',
            name='team_1',
        ),
        migrations.RemoveField(
            model_name='team2',
            name='team_2',
        ),
        migrations.AddField(
            model_name='match',
            name='team_1',
            field=models.ForeignKey(related_name='team1', default=0, to='playy.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='team_2',
            field=models.ForeignKey(related_name='team2', default=0, to='playy.Team'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Team1',
        ),
        migrations.DeleteModel(
            name='Team2',
        ),
    ]
