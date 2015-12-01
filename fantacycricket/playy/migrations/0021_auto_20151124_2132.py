# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0020_auto_20151124_2126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='match_name2',
            new_name='match_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='points',
        ),
    ]
