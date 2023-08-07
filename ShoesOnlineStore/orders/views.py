from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from orders.serializer import OrderItemsSerializer, CartItemsSerializer
from django.db.models import Subquery, OuterRef, Max
from shoes.models import Product, Price
from .cart import Cart


@csrf_exempt
@api_view(['POST'])
def add_to_cart(request):
    serializer = CartItemsSerializer(data=request.data)
    if serializer.is_valid():
        cart = Cart(request)
        product_id = serializer.validated_data.get('product_id', '')
        quantity = serializer.validated_data.get('quantity', '')

        last_price_subquery = Price.objects.filter(
            product=OuterRef('pk')).order_by('-create_timestamp')

        product = Product.objects.filter(id=product_id).select_related('brand', 'category').prefetch_related('color', 'size'
                                                                                                             ).annotate(
            last_price=Subquery(last_price_subquery.values('price')[:1])
        ).first()

        cart.add(product, quantity)
        return Response({'message': 'session_added'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
