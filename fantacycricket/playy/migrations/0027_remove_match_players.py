# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0026_match_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='players',
        ),
    ]
