from datetime import datetime

from rest_framework_jwt.compat import get_username_field
from rest_framework_jwt.settings import api_settings

def jwt_payload_handler(user):
    roles = []
    for group in user.groups.all():
        roles.append(group.name)
    payload = {
        'user_id': user.id,
        'username': user.username,
        'email': user.email, 
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
        'company_id': user.company.id,
        'roles': roles
        }
    return payload


def jwt_get_username_from_payload_handler(user):
    return user['email']
