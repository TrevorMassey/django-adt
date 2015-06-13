import uuid
from django.conf import settings
from django.core import validators
from model_utils import FieldTracker
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

from templated_email import send_templated_mail
from dossiers.models import Dossier, DossierRole


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          username=username,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True,
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
    username = models.CharField(_('username'), max_length=30, unique=True, db_index=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$', _('Enter a valid username.'), 'invalid')
        ])
    slug = AutoSlugField(populate_from='username', blank=True, db_index=True, overwrite=True, editable=True, unique=True)
    email = models.EmailField(_('email address'), unique=True, db_index=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    email_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    rank = models.ForeignKey('users.Rank', related_name='users', blank=True, null=True)
    rank_tracker = FieldTracker(fields=['rank'])
    avatar = models.ImageField(upload_to=user_image_path, blank=True, null=True, )

    email_key_expires = models.DateTimeField(blank=True, null=True)
    key = models.CharField(max_length=32, unique=True, blank=True, null=True)

    # External UIDS
    ts_uid = models.CharField(max_length=50, blank=True, null=True)  # tJL8iDNxG+1yeU5MQG61HnkC4nE=
    steam_id = models.CharField(max_length=20, blank=True, null=True)  # 76561197961103742

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['display_name', 'email']

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

    def generate_email_key(self):
        return uuid.uuid4().hex

    def send_verification_email(self):
        self.key = self.generate_email_key()
        self.email_key_expires = timezone.now() + timezone.timedelta(days=7)

        self.save()

        # TODO: send templated email

        context = {
            'user': self,
            'SITE_URL': settings.SITE_URL,
        }

        send_templated_mail(template_name='verification',
                            from_email='no-reply@addictguild.com',
                            recipient_list=[self.email],
                            context=context,)

    def create_dossier(self, creator):
        defaults = {
            'subject': self.display_name,
            'created_by': creator}
        dossier, created = Dossier.objects.get_or_create(subject_rel=self,
                                                         defaults=defaults)

        if not created:
            return

        for role_dict in self.user_roles.values():
            dossier_role = DossierRole(**role_dict)
            dossier_role.id = None
            dossier_role.subject_rel = dossier.id
            dossier_role.save()



def rank_image_path(instance, filename):
    path, ext = filename.split('.')
    return 'images/ranks/{filename}.{ext}'.format(filename=instance.title, ext=ext)

class Rank(models.Model):

    # Fields
    title = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='title', blank=True, unique=True)
    order = models.IntegerField(unique=True)
    image = models.ImageField(upload_to=rank_image_path)
    description = models.TextField()
    color = models.CharField(max_length=6)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.title

