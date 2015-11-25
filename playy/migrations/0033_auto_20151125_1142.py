# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0032_auto_20151125_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignPoints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match', models.ForeignKey(to='playy.Match')),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='match',
        ),
    ]
