from users.serializers import BasicUserSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': BasicUserSerializer(user).data
    }