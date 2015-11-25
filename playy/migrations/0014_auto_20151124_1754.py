# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0013_auto_20151124_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='match',
            name='team_1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team_2',
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='team2',
            name='team_2',
            field=models.ForeignKey(to='playy.Team'),
        ),
        migrations.AddField(
            model_name='team1',
            name='team_1',
            field=models.ForeignKey(to='playy.Team'),
        ),
    ]
