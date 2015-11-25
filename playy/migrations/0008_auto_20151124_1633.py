# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0007_auto_20151124_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='player_name',
            new_name='player1_name',
        ),
        migrations.AddField(
            model_name='team',
            name='player2_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='player3_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='player4_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
