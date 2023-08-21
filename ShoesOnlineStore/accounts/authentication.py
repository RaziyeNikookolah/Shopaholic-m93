import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed


User = get_user_model()


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        # Extract the JWT from the Authorization header
        authorization_header = request.headers.get("Authorization")
        if not authorization_header:
            raise AuthenticationFailed("Token not found")

        jwt_token = JWTAuthentication.get_the_token_from_header(
            authorization_header
        )  # clean the token
        # Decode the JWT and verify its signature
        try:
            payload = jwt.decode(
                jwt_token, settings.SECRET_KEY, algorithms=["HS256"])

        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed("Invalid signature")
        except jwt.exceptions.ExpiredSignatureError:
            raise AuthenticationFailed("Signature expired")
        except:
            raise AuthenticationFailed("Could not parse token")
        # Get the user from the database
        user_id = payload.get("user_id")
        if not user_id:
            raise AuthenticationFailed("User Id not found in JWT")
            # return None

        user = User.objects.filter(id=user_id).first()

        if not user:
            raise AuthenticationFailed("User not found")
        request.user = user
        # Return the user and token payload
        return user, payload

    def authenticate_header(self, request):
        return "Bearer"

    @classmethod
    def get_the_token_from_header(cls, token):
        token = token.replace("Bearer", "").replace(" ", "")  # clean the token
        return token


class LoginAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Extract the JWT from the Authorization header
        authorization_header = request.headers.get("Authorization")
        if not authorization_header:
            return None
        jwt_token = JWTAuthentication.get_the_token_from_header(
            authorization_header
        )  # clean the token
        # Decode the JWT and verify its signature
        payload = {}
        try:
            payload = jwt.decode(
                jwt_token, settings.SECRET_KEY, algorithms=["HS256"])

        except jwt.exceptions.ExpiredSignatureError:

            return None
        except:

            return None

        # Get the user from the database
        user_id = payload.get("user_id")
        if not user_id:
            return None

        user = User.objects.filter(id=user_id).first()

        if not user:
            return None
        # Return the user and token payload
        return user, payload

    def authenticate_header(self, request):
        return "Bearer"

    @classmethod
    def get_the_token_from_header(cls, token):
        token = token.replace("Bearer", "").replace(" ", "")  # clean the token
        return token
