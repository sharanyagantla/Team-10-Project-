# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0023_match_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='players',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team_1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team_2',
        ),
        migrations.AddField(
            model_name='team',
            name='match',
            field=models.ForeignKey(default=0, to='playy.Match'),
            preserve_default=False,
        ),
    ]
