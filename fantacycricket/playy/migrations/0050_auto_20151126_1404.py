# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0049_auto_20151126_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='team_1',
            field=models.ForeignKey(related_name='team1', to='playy.TeamPlayer'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_2',
            field=models.ForeignKey(related_name='team2', to='playy.TeamPlayer'),
        ),
    ]
