# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dossiers', '0003_auto_20150611_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='dossier',
            field=models.ForeignKey(default=1, to='dossiers.Dossier'),
            preserve_default=False,
        ),
    ]
