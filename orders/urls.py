from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

urlpatterns = []
shop_router = DefaultRouter()
shop_router.register('shop/orders', OrderViewSet)
urlpatterns += shop_router.urls