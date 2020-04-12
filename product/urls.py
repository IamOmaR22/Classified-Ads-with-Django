from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.productlist, name='product_list'),
    path('products/<slug:product_slug>/', views.productdetail, name='product_detail'),
]
