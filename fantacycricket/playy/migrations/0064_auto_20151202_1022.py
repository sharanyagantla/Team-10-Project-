# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0063_auto_20151201_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='img',
            field=models.ImageField(default=0, upload_to=b'pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='power_player',
            field=models.ForeignKey(related_name='pplayer', default=0, to='playy.Player'),
            preserve_default=False,
        ),
    ]
