# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='awardrecipient',
            name='awarder',
            field=models.ForeignKey(related_name='awarded', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='awardrecipient',
            name='recipient',
            field=models.ForeignKey(related_name='award_recipients', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='awardcategory',
            name='chapter',
            field=models.ForeignKey(to='games.Chapter'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='awardcategory',
            unique_together=set([('title', 'chapter')]),
        ),
        migrations.AddField(
            model_name='award',
            name='category',
            field=models.ForeignKey(to='awards.AwardCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='award',
            name='image',
            field=models.ForeignKey(to='awards.AwardImage'),
            preserve_default=True,
        ),
    ]
