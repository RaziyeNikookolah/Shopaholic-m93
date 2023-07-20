from django.urls import path
from . import views

urlpatterns = [
    path('/', views.ListCreateProductView.as_view(), name='product_list'),
    path('product_update/<int:pk>/',
         views.ProductUpdate.as_view(), name='product_update'),
]
