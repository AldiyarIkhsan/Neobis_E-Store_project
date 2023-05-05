from api.serializers.product import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from products.models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

