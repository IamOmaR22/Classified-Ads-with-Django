from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.productlist, name='product_list'),
    path('products/list/<int:id>/', views.productdetail, name='product_detail'),
]
