# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0037_auto_20151125_1248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='points',
            new_name='givepoints',
        ),
        migrations.AddField(
            model_name='givepoints',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
