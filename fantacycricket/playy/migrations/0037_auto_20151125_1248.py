# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0036_player_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='GivePoints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match', models.ForeignKey(to='playy.Match')),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='match',
        ),
        migrations.AlterField(
            model_name='player',
            name='points',
            field=models.ForeignKey(to='playy.GivePoints'),
        ),
    ]
