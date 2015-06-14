# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0006_auto_20150609_2255'),
        ('activityfeed', '0008_auto_20150613_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeditem',
            name='quote',
            field=models.ForeignKey(related_name='+', blank=True, to='multimedia.Quote', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feeditem',
            name='screenshot',
            field=models.ForeignKey(related_name='+', blank=True, to='multimedia.Screenshot', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feeditem',
            name='award',
            field=models.ForeignKey(related_name='+', blank=True, to='awards.Award', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feeditem',
            name='chapter',
            field=models.ForeignKey(related_name='+', blank=True, to='games.Chapter', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feeditem',
            name='feed_post',
            field=models.ForeignKey(related_name='+', blank=True, to='activityfeed.FeedPost', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feeditem',
            name='news',
            field=models.ForeignKey(related_name='+', blank=True, to='publications.News', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feeditem',
            name='rank',
            field=models.ForeignKey(related_name='+', blank=True, to='users.Rank', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feeditem',
            name='user',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
