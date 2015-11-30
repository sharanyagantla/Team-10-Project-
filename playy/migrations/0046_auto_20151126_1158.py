# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0045_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='home_address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='url',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='match',
            field=models.ForeignKey(default=0, to='playy.Match'),
            preserve_default=False,
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
    ]
