from rest_framework import viewsets
from backend.serializers import ProductSerializer
from backend.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('-date_created')
    serializer_class = ProductSerializer
