# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_poll_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['order'], 'verbose_name': 'choice', 'verbose_name_plural': 'choices'},
        ),
        migrations.AlterField(
            model_name='item',
            name='poll',
            field=models.ForeignKey(related_name='items', to='polls.Poll'),
            preserve_default=True,
        ),
    ]
