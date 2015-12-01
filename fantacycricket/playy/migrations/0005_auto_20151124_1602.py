# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0004_auto_20151124_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.AddField(
            model_name='team',
            name='player',
            field=models.ForeignKey(default=0, to='playy.Player'),
            preserve_default=False,
        ),
    ]
