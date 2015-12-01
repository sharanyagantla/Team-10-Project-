# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0042_asignpoints_team_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignpoints',
            name='team_name',
        ),
    ]
