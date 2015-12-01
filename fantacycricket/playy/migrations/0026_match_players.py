# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0025_auto_20151124_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='players',
            field=models.ForeignKey(default=0, to='playy.Player'),
            preserve_default=False,
        ),
    ]
