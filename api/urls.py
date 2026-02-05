from django.urls import path

from .views import (
    CategoryViewSet,
    ProductsView,
    ProductDetailView,
)


urlpatterns = [
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('products/', ProductsView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
