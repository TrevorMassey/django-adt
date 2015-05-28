# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import awards.models
import django_extensions.db.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_auto_20150527_0416'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwardImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True)),
                ('image', models.ImageField(upload_to=awards.models.award_image_path)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='award',
            name='image',
        ),
        migrations.AlterField(
            model_name='award',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='awardcategory',
            name='chapter',
            field=models.ForeignKey(to='games.Chapter'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='awardcategory',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='awardrecipient',
            name='recipient',
            field=models.ForeignKey(related_name='award_recipients', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='awardcategory',
            unique_together=set([('title', 'chapter')]),
        ),
    ]
