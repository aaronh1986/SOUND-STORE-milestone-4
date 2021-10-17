from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.admin_product_add, name='admin_product_add'),
    path('edit/<int:product_id>/', views.admin_product_edit, name='admin_product_edit'),
]
