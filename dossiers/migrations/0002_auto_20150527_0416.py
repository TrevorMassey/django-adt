# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
        ('dossiers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='game',
            field=models.ForeignKey(to='games.Game'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='role',
            name='guild',
            field=models.ForeignKey(to='dossiers.Guild'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guild',
            name='game',
            field=models.OneToOneField(to='games.Game'),
            preserve_default=True,
        ),
    ]
