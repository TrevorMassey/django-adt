# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_codex_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codex',
            name='article',
            field=models.OneToOneField(null=True, blank=True, to='publications.Article'),
            preserve_default=True,
        ),
    ]
