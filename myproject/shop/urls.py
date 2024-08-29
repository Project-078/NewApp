from django.urls import path
from . import views

urlpatterns = [
    
    path('product', views.product, name='product'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('categories/', views.category_list, name='category_list'),
    
]
