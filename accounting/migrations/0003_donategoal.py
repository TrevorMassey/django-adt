# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_donateamount_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonateGoal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=9, decimal_places=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
    ]
