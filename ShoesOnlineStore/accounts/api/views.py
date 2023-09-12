from django.shortcuts import get_object_or_404
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ViewSet
from django.views.decorators.csrf import csrf_exempt
from ..models import Account, Address, Profile
from .serializers import AccountSerializer, AddressSerializer, ProfileSerializer
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


class ProfileViewSet(ViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @csrf_exempt
    def update(self, request, pk):
        account = get_object_or_404(Account, pk=pk)
        profile = get_object_or_404(Profile, account=account)
        serializer = ProfileSerializer(
            instance=profile, data=request.data, partial=True)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


router.register(r'profiles', ProfileViewSet, basename='profile')


class AddressViewSet(ViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    @csrf_exempt
    def create(self, request):
        serializer = AddressSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(request.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def update(self, request, pk):
        address = get_object_or_404(Address, pk=pk)
        serializer = AddressSerializer(
            instance=address, data=request.data, partial=True)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def destroy(self, request, pk):
        address = get_object_or_404(Address, pk=pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


router.register(r'addresses', AddressViewSet, basename='address')
