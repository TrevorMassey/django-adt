# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20150602_0212'),
        ('publications', '0005_auto_20150601_0411'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0004_auto_20150601_0400'),
        ('games', '0002_chapter_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=15, choices=[(b'feed_post', b'New Feed Post'), (b'forum_post', b'New Forum Post'), (b'join', b'Joined Guild'), (b'screenshot', b'Uploaded Screenshot'), (b'video', b'New Video'), (b'quote', b'New Quote'), (b'chapter', b'New Chapter'), (b'promotion', b'Promoted'), (b'award', b'New Award Recipient')])),
                ('public', models.BooleanField(default=False)),
                ('created', models.DateField(default=django.utils.timezone.now)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_time', models.DateTimeField(null=True, blank=True)),
                ('award_recipient', models.ForeignKey(blank=True, to='awards.AwardRecipient', null=True)),
                ('chapter', models.ForeignKey(blank=True, to='games.Chapter', null=True)),
                ('deleted_by', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeedPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='feeditem',
            name='feed_post',
            field=models.ForeignKey(blank=True, to='activityfeed.FeedPost', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feeditem',
            name='news',
            field=models.ForeignKey(blank=True, to='publications.News', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feeditem',
            name='rank',
            field=models.ForeignKey(blank=True, to='users.Rank', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feeditem',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
