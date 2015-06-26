# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dkp', '0004_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventitem',
            name='attendee',
        ),
        migrations.AddField(
            model_name='eventitem',
            name='user',
            field=models.ForeignKey(related_name='awarded_items', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bonus',
            name='dkp',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entity',
            name='dkp',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventitem',
            name='dkp',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='dkp',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='dkp',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='credit',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='debit',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
