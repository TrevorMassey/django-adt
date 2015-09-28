# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLog',
            fields=[
                ('record', models.IntegerField(serialize=False, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('timestamp', models.IntegerField()),
                ('type', models.IntegerField()),
                ('action', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'admin_log',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameHistory',
            fields=[
                ('record', models.IntegerField(serialize=False, primary_key=True)),
                ('user', models.IntegerField()),
                ('starttime', models.IntegerField()),
                ('stoptime', models.IntegerField()),
            ],
            options={
                'db_table': 'game_history',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WebsiteLogin',
            fields=[
                ('record', models.IntegerField(serialize=False, primary_key=True)),
                ('timestamp', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('ip', models.CharField(max_length=100)),
                ('account', models.IntegerField()),
                ('success', models.IntegerField()),
            ],
            options={
                'db_table': 'website_login',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
