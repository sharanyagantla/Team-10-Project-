# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0040_remove_player_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignPoints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField(default=0)),
                ('match', models.ForeignKey(to='playy.Match')),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='points',
        ),
        migrations.AddField(
            model_name='asignpoints',
            name='playername',
            field=models.ForeignKey(to='playy.Player'),
        ),
    ]
