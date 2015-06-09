# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multimedia.models


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='image',
            field=models.ImageField(null=True, upload_to=multimedia.models.quote_image_path, blank=True),
            preserve_default=True,
        ),
    ]
