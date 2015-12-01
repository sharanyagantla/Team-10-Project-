# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0005_auto_20151124_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='player',
            new_name='player1',
        ),
    ]
