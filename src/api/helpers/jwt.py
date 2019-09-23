from datetime import datetime

from rest_framework_jwt.compat import get_username_field
from rest_framework_jwt.settings import api_settings

def jwt_payload_handler(user):
    payload = {
        'user_id': user.id,
        'username': user.email,
        'email': user.email, 
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
        'company_id': user.company_id
        }
    return payload
