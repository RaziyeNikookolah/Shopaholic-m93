from django.shortcuts import get_object_or_404
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ViewSet
from ..models import Account
from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework.views import APIView, status
from accounts.utils import generate_access_token, generate_refresh_token


class TokenObtainPairView(APIView):

    def get(self, request):
        if user := request.user:
            access_token = generate_access_token(user, 3)
            refresh_token = generate_refresh_token(user, 30)
            return Response({"access_token": access_token, "refresh_token": refresh_token}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "No Token Generated "}, status=status.HTTP_204_NO_CONTENT)


class AccountViewSet(ViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # http_method_names = ['get']

    def list(self, request):
        serializer = AccountSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        account = get_object_or_404(Account, pk=pk)
        serializer = AccountSerializer(instance=account)
        return Response(serializer.data, status=status.HTTP_200_OK)


router = DefaultRouter()
router.register(r'accounts', AccountViewSet, basename='account')


class get_user_id_in_token(APIView):
    def get(self, request):
        return Response({"userId": request.user.id})
