from django.utils.translation import ugettext_lazy as _
from django.db import models
from django_extensions.db.fields import AutoSlugField

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)

def user_image_path(instance, filename):
    path, ext = filename.split('.')
    return 'images/avatars/{filename}.{ext}'.format(filename=instance.display_name, ext=ext)


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username, password and email are required. Other fields are optional.
    """

    display_name = models.CharField(max_length=30)
    email = models.EmailField(_('email address'), unique=True, db_index=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    email_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    rank = models.OneToOneField('users.Rank', null=True, blank=True)
    avatar = models.ImageField(upload_to=user_image_path)

    email_key_expires = models.DateTimeField(blank=True, null=True)
    key = models.CharField(max_length=40, unique=True, blank=True, null=True)

    # External UIDS
    ts_uid = models.CharField(max_length=50, blank=True, null=True)  # tJL8iDNxG+1yeU5MQG61HnkC4nE=
    steam_id = models.CharField(max_length=20, blank=True, null=True)  # 76561197961103742

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['display_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return self.display_name

    def get_short_name(self):
        "Returns the short name for the user."
        return self.display_name

    def __unicode__(self):
        return u'%s' % self.display_name


def rank_image_path(instance, filename):
    path, ext = filename.split('.')
    return 'images/ranks/{filename}.{ext}'.format(filename=instance.number, ext=ext)

class Rank(models.Model):

    # Fields
    title = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='title', blank=True, unique=True)
    number = models.IntegerField()
    image = models.ImageField(upload_to=rank_image_path)
    description = models.TextField()
    color = models.CharField(max_length=6)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.title

