from django.urls import include, path
from rest_framework import routers
from .viewset import ProductViewSet, CategoryViewSet, ProductImageViewSet


router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('productimage', ProductImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]