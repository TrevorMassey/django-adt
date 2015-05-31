# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationquestion',
            name='chapter',
            field=models.ForeignKey(to='games.Chapter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicationanswer',
            name='question',
            field=models.OneToOneField(to='applications.ApplicationQuestion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='answers',
            field=models.ManyToManyField(to='applications.ApplicationQuestion'),
            preserve_default=True,
        ),
    ]
