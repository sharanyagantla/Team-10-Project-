# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0012_auto_20151124_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='team_2',
            field=models.TextField(default=0, verbose_name=b'Team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='team_1',
            field=models.TextField(verbose_name=b'Team'),
        ),
    ]
