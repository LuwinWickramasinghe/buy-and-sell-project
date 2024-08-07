from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.index),
    path('products/', views.products),
    path('products/<int:id>/', views.product_detail)
]
