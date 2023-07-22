from .models import Product
from .serializer import ProductsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# IsAuthenticatedOrReadOnly permission just can run safe method for unauthenticated user
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListCreateProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = ((IsAuthenticatedOrReadOnly,))


class ProductUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = ((IsAuthenticatedOrReadOnly,))
