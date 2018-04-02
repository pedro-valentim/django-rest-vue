from rest_framework import serializers
from backend.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock_quantity', 'photo')
