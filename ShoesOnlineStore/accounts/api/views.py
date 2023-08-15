from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView, status
from rest_framework.permissions import AllowAny
from accounts.utils import generate_access_token, generate_refresh_token


class TokenObtainPairView(APIView):

    def get(self, request):
        if user := request.user:
            access_token = generate_access_token(user, 3)
            refresh_token = generate_refresh_token(user, 30)
            return Response({"access_token": access_token, "refresh_token": refresh_token}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "No Token Generated "}, status=status.HTTP_204_NO_CONTENT)


# class AccessTokenView(APIView):

#     def get(self, request):
#         if user := request.user:
#             access_token = generate_access_token(user, 3)
#             return Response({"access_token": access_token}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"message": "No Token Generated "}, status=status.HTTP_204_NO_CONTENT)


# class RefreshTokenView(APIView):

#     def get(self, request):
#         if user := request.user:
#             refresh_token = generate_refresh_token(user, 3)
#             return Response({"refresh_token": refresh_token}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"message": "No Token Generated "}, status=status.HTTP_204_NO_CONTENT)
# class LoginOrRegisterView(APIView):
#     permission_classes=[AllowAny]
#     authentication_classes=[]
#     def post(self,request):
