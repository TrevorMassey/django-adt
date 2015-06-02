# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_application_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='state',
            field=django_fsm.FSMField(default=b'step_1_submitted', max_length=50),
            preserve_default=True,
        ),
    ]
