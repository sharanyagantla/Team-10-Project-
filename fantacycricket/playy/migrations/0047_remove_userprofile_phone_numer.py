# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0046_auto_20151126_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='phone_numer',
        ),
    ]
