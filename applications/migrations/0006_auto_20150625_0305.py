# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0005_application_chapter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='answers',
        ),
        migrations.AddField(
            model_name='applicationanswer',
            name='application',
            field=models.ForeignKey(related_name='answers', default=1, to='applications.Application'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationanswer',
            name='question',
            field=models.ForeignKey(to='applications.ApplicationQuestion'),
            preserve_default=True,
        ),
    ]
