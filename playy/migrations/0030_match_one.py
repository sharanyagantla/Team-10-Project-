# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0029_remove_match_one'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='one',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
