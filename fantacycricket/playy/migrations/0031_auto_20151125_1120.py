# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0030_match_one'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='one',
        ),
        migrations.AddField(
            model_name='match',
            name='player1_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='player2_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='player3_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='player4_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='player_1',
            field=models.ForeignKey(related_name='player1', default=0, to='playy.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='player_2',
            field=models.ForeignKey(related_name='player2', default=0, to='playy.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='player_3',
            field=models.ForeignKey(related_name='player3', default=0, to='playy.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='player_4',
            field=models.ForeignKey(related_name='player4', default=0, to='playy.Player'),
            preserve_default=False,
        ),
    ]
