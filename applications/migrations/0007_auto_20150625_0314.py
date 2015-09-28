# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0006_auto_20150625_0305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicationquestion',
            options={'ordering': ('-order',)},
        ),
        migrations.RemoveField(
            model_name='applicationquestion',
            name='created',
        ),
        migrations.RemoveField(
            model_name='applicationquestion',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='applicationquestion',
            name='slug',
        ),
    ]
