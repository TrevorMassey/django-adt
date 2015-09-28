import logging

from rest_framework import exceptions
from rest_framework_jwt import utils
from rest_framework_jwt.settings import api_settings
from swampdragon.connections.sockjs_connection import DjangoSubscriberConnection

logger = logging.getLogger(__name__)


jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_user_id_from_payload = api_settings.JWT_PAYLOAD_GET_USER_ID_HANDLER


class JWTDataConnection(DjangoSubscriberConnection):

    def __init__(self, session):
        self._user = None
        super(JWTDataConnection, self).__init__(session)

    def on_close(self):
        if self.user:
            logger.info("Closed connection for user: %s", self.user)

        super(JWTDataConnection, self).on_close()

    def on_open(self, request):
        logger.info("Opened connection: %s", request)
        super(JWTDataConnection, self).on_open(request)

    def get_user(self):
        return self._user

    @property
    def user(self):
        return self.get_user()

    def authenticate(self, token):
        payload = jwt_decode_handler(token)
        try:
            self._user = self.authenticate_credentials(payload)
        except exceptions.AuthenticationFailed:
            self._user = None

    def authenticate_credentials(self, payload):
        """
        Returns an active user that matches the payload's user id and email.
        """
        User = utils.get_user_model()

        user_id = jwt_get_user_id_from_payload(payload)

        if user_id is not None:
            try:
                user = User.objects.get(pk=user_id, is_active=True)
            except User.DoesNotExist:
                msg = _('Invalid signature.')
                raise exceptions.AuthenticationFailed(msg)
        else:
            msg = _('Invalid payload.')
            raise exceptions.AuthenticationFailed(msg)

        return user
