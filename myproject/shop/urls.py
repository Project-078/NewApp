from django.urls import path
from . import views

urlpatterns = [
     path('', views.lgn, name='lgn'),
    path('login/', views.login, name='login'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('register/',views.register,name='register')
]
