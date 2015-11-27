# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match', models.ForeignKey(to='login.Match')),
                ('player_1', models.ForeignKey(related_name='player1', to='login.Player')),
                ('player_2', models.ForeignKey(related_name='player2', to='login.Player')),
                ('player_3', models.ForeignKey(related_name='player3', to='login.Player')),
                ('player_4', models.ForeignKey(related_name='player4', to='login.Player')),
                ('player_5', models.ForeignKey(related_name='player5', to='login.Player')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
