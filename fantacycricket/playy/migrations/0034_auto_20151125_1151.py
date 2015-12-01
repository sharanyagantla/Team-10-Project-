# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0033_auto_20151125_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignpoints',
            name='players',
            field=models.ForeignKey(default=0, to='playy.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignpoints',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
