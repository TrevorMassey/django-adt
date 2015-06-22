# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_donategoal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donatecost',
            name='slug',
        ),
    ]
