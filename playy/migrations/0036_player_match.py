# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0035_auto_20151125_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='match',
            field=models.ForeignKey(default=0, to='playy.Match'),
            preserve_default=False,
        ),
    ]
