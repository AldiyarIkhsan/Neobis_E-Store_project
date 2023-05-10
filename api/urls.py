from rest_framework.routers import DefaultRouter
from api.views.product import ProductViewSet
from api.views.product_category import ProductCategoryViewSet


urlpatterns = []
shop_router = DefaultRouter()
shop_router.register('shop/products', ProductViewSet)
shop_router.register('shop/categories', ProductCategoryViewSet)
urlpatterns += shop_router.urls


