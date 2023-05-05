from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.views.product import ProductViewSet
from api.views.product_category import ProductCategoryViewSet


urlpatterns = []
shop_router = SimpleRouter()
shop_router.register('shop/products', ProductViewSet)
shop_router.register('shop/categories', ProductCategoryViewSet)
urlpatterns += shop_router.urls


