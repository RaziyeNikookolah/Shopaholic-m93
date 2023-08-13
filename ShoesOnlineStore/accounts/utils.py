import jwt
import datetime
from django.conf import settings


def generate_access_token(user, expiration_time_minutes=5):
    access_token_payload = {
        "user_id": user.id,
        "exp": datetime.datetime.utcnow()
        + datetime.timedelta(days=0, minutes=expiration_time_minutes),
        "iat": datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(
        access_token_payload, settings.SECRET_KEY, algorithm="HS256"
    )

    return access_token


def generate_refresh_token(user, expiration_time_days=10):
    refresh_token_payload = {
        "user_id": user.id,
        "exp": datetime.datetime.utcnow()
        + datetime.timedelta(days=expiration_time_days),
        "iat": datetime.datetime.utcnow(),
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.REFRESH_TOKEN_SECRET, algorithm="HS256"
    )
    return refresh_token
