# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0038_auto_20151125_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='givepoints',
            name='match',
        ),
        migrations.RemoveField(
            model_name='player',
            name='givepoints',
        ),
        migrations.AddField(
            model_name='player',
            name='match',
            field=models.ForeignKey(default=0, to='playy.Match'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='GivePoints',
        ),
    ]
