# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0058_auto_20151129_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertotpoints',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserTotpoints',
        ),
    ]
