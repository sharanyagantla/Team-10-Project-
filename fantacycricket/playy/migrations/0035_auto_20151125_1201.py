# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0034_auto_20151125_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignpoints',
            name='match',
        ),
        migrations.RemoveField(
            model_name='assignpoints',
            name='players',
        ),
        migrations.AddField(
            model_name='player',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='AssignPoints',
        ),
    ]
