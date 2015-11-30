# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0050_auto_20151126_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamplayer',
            name='player_1',
        ),
        migrations.RemoveField(
            model_name='teamplayer',
            name='player_2',
        ),
        migrations.RemoveField(
            model_name='teamplayer',
            name='player_3',
        ),
        migrations.RemoveField(
            model_name='teamplayer',
            name='player_4',
        ),
        migrations.RemoveField(
            model_name='teamplayer',
            name='team',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='uplayer_1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='uplayer_2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='uplayer_3',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='uplayer_4',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='uplayer_5',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='player_1',
            field=models.ForeignKey(related_name='player1', default=0, to='playy.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='player_2',
            field=models.ForeignKey(related_name='player2', default=0, to='playy.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='player_3',
            field=models.ForeignKey(related_name='player3', default=0, to='playy.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='player_4',
            field=models.ForeignKey(related_name='player4', default=0, to='playy.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='player_5',
            field=models.ForeignKey(related_name='player5', default=0, to='playy.Player'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='team_1',
            field=models.ForeignKey(related_name='team1', to='playy.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_2',
            field=models.ForeignKey(related_name='team2', to='playy.Team'),
        ),
        migrations.DeleteModel(
            name='TeamPlayer',
        ),
    ]
