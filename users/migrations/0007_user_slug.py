# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20150602_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(populate_from=models.CharField(max_length=30), editable=False, blank=True),
            preserve_default=True,
        ),
    ]
