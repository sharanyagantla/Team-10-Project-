# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0016_auto_20151124_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_2', models.ForeignKey(to='playy.Team')),
            ],
        ),
        migrations.RemoveField(
            model_name='match',
            name='team_1',
        ),
        migrations.RemoveField(
            model_name='team1',
            name='match_name',
        ),
        migrations.AddField(
            model_name='match',
            name='match_name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team1',
            name='team_1',
            field=models.ForeignKey(default=0, to='playy.Team'),
            preserve_default=False,
        ),
    ]
