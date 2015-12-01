# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0041_auto_20151125_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignpoints',
            name='team_name',
            field=models.ForeignKey(default=0, to='playy.Team'),
            preserve_default=False,
        ),
    ]
