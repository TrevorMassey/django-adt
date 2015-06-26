# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dkp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='boss',
            new_name='entity',
        ),
        migrations.AddField(
            model_name='resource',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entity',
            name='location',
            field=models.ForeignKey(related_name='entities', to='dkp.Location'),
            preserve_default=True,
        ),
    ]
