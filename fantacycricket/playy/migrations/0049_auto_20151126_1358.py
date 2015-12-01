# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0048_auto_20151126_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamplayer',
            name='player_5',
        ),
        migrations.RemoveField(
            model_name='teamplayer',
            name='player_6',
        ),
        migrations.RemoveField(
            model_name='teamplayer',
            name='player_7',
        ),
    ]
