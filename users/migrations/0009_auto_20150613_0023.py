# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20150612_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=30, validators=[django.core.validators.RegexValidator(b'^[\\w.@+-]+$', 'Enter a valid username.', b'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username', db_index=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'username', blank=True, unique=True, overwrite=True),
            preserve_default=True,
        ),
    ]
