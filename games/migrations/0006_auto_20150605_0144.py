# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0005_auto_20150605_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChapterDivision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='games.ChapterDivision', null=True)),
            ],
            options={
                'ordering': ('-id',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChapterRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=255, null=True, blank=True)),
                ('division', models.ForeignKey(to='games.ChapterDivision')),
                ('member', models.ForeignKey(related_name='role', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='chaptermember',
            options={'ordering': ('-id',)},
        ),
    ]
