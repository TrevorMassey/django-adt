# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dossiers', '0007_note_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossier',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'subject', blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guild',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guild',
            name='title',
            field=models.CharField(unique=True, max_length=255),
            preserve_default=True,
        ),
    ]
