# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsignPoints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date of match')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='login.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_1',
            field=models.ForeignKey(related_name='team1', to='login.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_2',
            field=models.ForeignKey(related_name='team2', to='login.Team'),
        ),
        migrations.AddField(
            model_name='asignpoints',
            name='match',
            field=models.ForeignKey(to='login.Match'),
        ),
        migrations.AddField(
            model_name='asignpoints',
            name='playername',
            field=models.ForeignKey(to='login.Player'),
        ),
    ]
