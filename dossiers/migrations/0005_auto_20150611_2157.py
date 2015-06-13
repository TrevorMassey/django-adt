# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dossiers', '0004_note_dossier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossierrole',
            name='dossier',
            field=models.ForeignKey(related_name='roles', to='dossiers.Dossier'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='dossier',
            field=models.ForeignKey(related_name='notes', to='dossiers.Dossier'),
            preserve_default=True,
        ),
    ]
