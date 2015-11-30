# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0043_remove_asignpoints_team_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignpoints',
            name='team',
            field=models.ForeignKey(default=0, to='playy.Team'),
            preserve_default=False,
        ),
    ]
