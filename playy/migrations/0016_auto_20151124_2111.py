# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0015_auto_20151124_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_name',
        ),
    ]
