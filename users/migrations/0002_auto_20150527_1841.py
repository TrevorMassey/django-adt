# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='image',
            field=models.ImageField(upload_to=users.models.rank_image_path),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rank',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rank',
            name='title',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
