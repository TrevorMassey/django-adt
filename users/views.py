import logging

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.utils import timezone
from django.views.generic import View
from users.models import User

logger = logging.getLogger(__name__)

class UserVerifyEmailView(View):
    success_template = 'users/verify_success.html'
    error_template = 'users/verify_error.html'

    def render_to_response(self, template_name, context=None):

        if not context:
            context = {}

        return render_to_response(template_name, context)

    def get(self, request, **kwargs):

        key = kwargs.get('key')

        logger.info(key)

        try:
            user = User.objects.get(key=key)
        except User.DoesNotExist:
            return self.render_to_response(template_name=self.error_template, context={'reason': "Key not found."})

        if user.email_key_expires > timezone.now():

            logger.info("User %s" % user)
            # Key found and is not expired
            user.email_verified = True
            user.key = None
            user.email_key_expires = None
            user.save()

            return self.render_to_response(template_name=self.success_template, context={'user': user})

        return self.render_to_response(template_name=self.error_template)


verify_email = UserVerifyEmailView.as_view()
