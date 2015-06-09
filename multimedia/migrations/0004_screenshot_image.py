# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150609_0001'),
        ('multimedia', '0003_auto_20150609_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenshot',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='screenshot', default=1, to='filer.Image'),
            preserve_default=False,
        ),
    ]
