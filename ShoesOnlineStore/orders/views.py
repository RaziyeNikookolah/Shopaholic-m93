from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from orders.serializer import OrderItemsSerializer, AddCartItemsSerializer, RemoveCartItemsSerializer, CartItemSerializer
from django.db.models import Subquery, OuterRef
from shoes.models import Product, Price
from .cart import Cart, CART_SESSION_ID


cart = {}


@csrf_exempt
@api_view(['POST'])
def add_to_cart(request):
    serializer = AddCartItemsSerializer(data=request.data)
    if serializer.is_valid():
        global cart
        cart = Cart(request)
        product_id = serializer.validated_data.get('product_id', '')
        quantity = serializer.validated_data.get('quantity', '')
        color = serializer.validated_data.get('color', '')
        image = serializer.validated_data.get('image', '')
        size = serializer.validated_data.get('size', '')
        price = serializer.validated_data.get('price', '')

        last_price_subquery = Price.objects.filter(
            product=OuterRef('pk')).order_by('-create_timestamp')

        product = Product.objects.filter(id=product_id).select_related('brand', 'category').prefetch_related('color', 'size'
                                                                                                             ).annotate(
            last_price=Subquery(last_price_subquery.values('price')[:1])
        ).filter(color__name=color, size__number=size).first()

        cart.add(product, quantity, size, image, color, str(price))
        return Response({'message': 'item_added'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def remove_from_cart(request):
    serializer = RemoveCartItemsSerializer(data=request.data)
    product_id = serializer.validated_data.get('product_id', '')
    if serializer.is_valid():
        cart.remove(product_id)
        return Response({'message': 'cart item removed'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def cart_list(request):
    global cart
    cart.print()
    serializer = CartItemSerializer(cart, many=True)
    serialized_data = serializer.data

    return Response(serialized_data)
