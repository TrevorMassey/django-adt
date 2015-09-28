# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dkp', '0011_transaction_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='attendance',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dkp.EventAttendance', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='bonus',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dkp.Bonus', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='entity',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dkp.EventEntity', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='item',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dkp.EventItem', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='resource_contrib',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dkp.ResourceContrib', null=True),
            preserve_default=True,
        ),
    ]
