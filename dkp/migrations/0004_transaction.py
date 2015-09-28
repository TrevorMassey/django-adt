# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dkp', '0003_event_standby_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('credit', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('debit', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('attendance', models.ForeignKey(related_name='+', blank=True, to='dkp.EventAttendance', null=True)),
                ('entity', models.ForeignKey(related_name='+', blank=True, to='dkp.EventEntity', null=True)),
                ('event', models.ForeignKey(related_name='+', blank=True, to='dkp.Event', null=True)),
                ('item', models.ForeignKey(related_name='+', blank=True, to='dkp.EventItem', null=True)),
                ('resource_contrib', models.ForeignKey(related_name='+', blank=True, to='dkp.ResourceContrib', null=True)),
                ('user', models.ForeignKey(related_name='dkp_transactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'transaction',
                'verbose_name_plural': 'transactions',
            },
            bases=(models.Model,),
        ),
    ]
