from orders.serializers import OrderSerializer
from rest_framework.viewsets import ModelViewSet
from orders.models import Order


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer