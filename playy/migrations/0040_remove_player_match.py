# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0039_auto_20151125_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='match',
        ),
    ]
