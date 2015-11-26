# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='team',
            old_name='player_name',
            new_name='team_name',
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(to='playy.Player'),
        ),
    ]
