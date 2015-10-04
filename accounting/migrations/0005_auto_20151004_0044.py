# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_remove_donatecost_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donatecost',
            name='last_updated',
        ),
        migrations.AlterField(
            model_name='donateamount',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
