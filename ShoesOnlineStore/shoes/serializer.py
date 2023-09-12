from rest_framework import serializers
from .models import Product


class ProductsSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)
    color = serializers.StringRelatedField(many=True, read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    size = serializers.StringRelatedField(many=True, read_only=True)
    available_quantity = serializers.StringRelatedField(read_only=True)
    last_price = serializers.StringRelatedField(read_only=True)
    gallery = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductSimpleSerializer(serializers.ModelSerializer):
    # price = serializers.StringRelatedField(read_only=True)
    size = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'size',  # 'price',
                  'image')
