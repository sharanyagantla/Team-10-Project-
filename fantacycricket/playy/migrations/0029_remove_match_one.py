# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0028_match_one'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='one',
        ),
    ]
