# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0006_auto_20151124_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='player1',
        ),
        migrations.AddField(
            model_name='team',
            name='player_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]
