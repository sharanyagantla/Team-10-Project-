# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0047_remove_userprofile_phone_numer'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamPlayer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_1', models.ForeignKey(related_name='player1', to='playy.Player')),
                ('player_2', models.ForeignKey(related_name='player2', to='playy.Player')),
                ('player_3', models.ForeignKey(related_name='player3', to='playy.Player')),
                ('player_4', models.ForeignKey(related_name='player4', to='playy.Player')),
                ('player_5', models.ForeignKey(related_name='player5', to='playy.Player')),
                ('player_6', models.ForeignKey(related_name='player6', to='playy.Player')),
                ('player_7', models.ForeignKey(related_name='player7', to='playy.Player')),
                ('team', models.ForeignKey(to='playy.Team')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='player_1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='player_2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='player_3',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='player_4',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='player_5',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='uplayer_1',
            field=models.ForeignKey(related_name='uplayer_1', default=0, to='playy.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='uplayer_2',
            field=models.ForeignKey(related_name='uplayer_2', default=0, to='playy.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='uplayer_3',
            field=models.ForeignKey(related_name='uplayer_3', default=0, to='playy.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='uplayer_4',
            field=models.ForeignKey(related_name='uplayer_4', default=0, to='playy.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='uplayer_5',
            field=models.ForeignKey(related_name='uplayer_5', default=0, to='playy.Player'),
            preserve_default=False,
        ),
    ]
