from api.serializers.product_category import ProductCategorySerializer
from rest_framework.viewsets import ModelViewSet
from products.models import ProductCategory


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer