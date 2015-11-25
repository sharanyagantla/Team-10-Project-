# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0003_auto_20151124_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'date of match'),
        ),
    ]
