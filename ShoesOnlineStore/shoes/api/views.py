from shoes.models import Category
from shoes.api.serializers import CategorySerializer
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class ListCategory(ViewSet):
    queryset = Category.objects.all()
    http_method_names = ['get']

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


router = DefaultRouter()
router.register(r'categories', ListCategory, basename='category')
