# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_auto_20150613_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapterdivision',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chaptermember',
            name='division',
            field=models.ForeignKey(related_name='members', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='games.ChapterDivision', null=True),
            preserve_default=True,
        ),
    ]
