# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multimedia.models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0004_screenshot_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='image',
            field=models.ImageField(upload_to=multimedia.models.screenshot_image_path),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True),
            preserve_default=True,
        ),
    ]
