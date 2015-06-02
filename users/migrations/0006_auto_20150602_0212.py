# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150602_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=users.models.user_image_path, blank=True),
            preserve_default=True,
        ),
    ]
