# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0060_points'),
    ]

    operations = [
        migrations.RenameField(
            model_name='points',
            old_name='points',
            new_name='full_points',
        ),
    ]
