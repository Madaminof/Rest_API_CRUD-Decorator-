from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryList),
    path('product/<int:pk>/', views.ProductDetail),
]