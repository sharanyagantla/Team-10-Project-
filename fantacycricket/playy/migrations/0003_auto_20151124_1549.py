# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0002_auto_20151124_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='members',
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default=0, to='playy.Team'),
            preserve_default=False,
        ),
    ]
