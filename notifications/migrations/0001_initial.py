# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20150602_0212'),
        ('games', '0008_auto_20150605_0219'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0004_auto_20150601_0400'),
        ('applications', '0005_application_chapter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=30, choices=[(b'username_mention_comment', b'Username Mentioned in Comment'), (b'username_mention_forum', b'Username Mentioned in Forum Post'), (b'application', b'Application Status Change'), (b'award', b'Received Award'), (b'promoted', b'Received Promotion'), (b'demoted', b'Received Demotion'), (b'event', b'New Event'), (b'kicked', b'Kicked from guild'), (b'quote', b'You were quoted'), (b'screenshot', b'You were tagged in a screenshot'), (b'chapter', b'You were added to a chapter')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('application', models.ForeignKey(blank=True, to='applications.Application', null=True)),
                ('award', models.ForeignKey(blank=True, to='awards.Award', null=True)),
                ('chapter', models.ForeignKey(blank=True, to='games.Chapter', null=True)),
                ('creator', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('rank', models.ForeignKey(blank=True, to='users.Rank', null=True)),
                ('user', models.ForeignKey(related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
