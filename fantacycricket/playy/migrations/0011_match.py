# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playy', '0010_auto_20151124_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date of match')),
            ],
        ),
    ]
