from django.db import models
from django_extensions.db.fields import AutoSlugField


class Guild(models.Model):

    # Fields
    title = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

class Role(models.Model):

    # Fields
    role = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    duration = models.PositiveIntegerField()

    # Relationship Fields
    guild = models.ForeignKey('dossiers.Guild', related_name="%(app_label)s_%(class)s_guild")
    game = models.ForeignKey('games.Game', related_name="%(app_label)s_%(class)s_game")

    class Meta:
        abstract = True
        ordering = ('-created',)

class UserRole(Role):
    user = models.ForeignKey('users.User', related_name='roles')

    def __unicode__(self):
        return u'%s' % self.role


class DossierRole(Role):
    dossier = models.ForeignKey('dossiers.Dossier', related_name='roles')

    def __unicode__(self):
        return u'%s' % self.role


class Dossier(models.Model):

    # Subject may not be a user on this website (dossier on enemy leader)
    subject = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='subject', unique=True)
    # Only one Dossier per user
    subject_rel = models.OneToOneField('users.User', related_name='dossier', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', related_name='+')

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug


class Heading(models.Model):
    title = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', related_name='+')

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.title

class Note(models.Model):

    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', related_name='dossier_notes')

    heading = models.ForeignKey('dossiers.Heading',)
    dossier = models.ForeignKey('dossiers.Dossier', related_name='notes')
    game = models.ForeignKey('games.Game', related_name='+')

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return '%s...' % self.body[10:].strip()


class Issue(models.Model):

    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', related_name='+')

    chapter = models.ForeignKey('games.Chapter', related_name='+', blank=True, null=True)
    involved = models.ManyToManyField('users.User', related_name='issues')

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return '%s...' % self.description[10:].strip()
