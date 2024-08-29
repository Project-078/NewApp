from django.urls import path
from . import views

urlpatterns = [
#     path('', views.login, name='login'),
#     path('product/<slug:slug>/', views.product_detail, name='product_detail'),
#     path('categories/', views.category_list, name='category_list'),

    path('',views.index, name='index')
]
