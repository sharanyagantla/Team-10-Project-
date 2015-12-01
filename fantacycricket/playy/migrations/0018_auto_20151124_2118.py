# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0017_auto_20151124_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team2',
            name='team_2',
        ),
        migrations.AddField(
            model_name='team1',
            name='test',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Team2',
        ),
    ]
