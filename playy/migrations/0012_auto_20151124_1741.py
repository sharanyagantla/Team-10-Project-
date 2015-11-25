# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0011_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='team_1',
            field=models.ForeignKey(default=0, to='playy.Team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.TextField(max_length=200),
        ),
    ]
