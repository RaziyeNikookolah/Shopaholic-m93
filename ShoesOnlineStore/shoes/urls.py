from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.ProductList.as_view(), name='product_list'),
    path('product_details/<int:pk>/',
         views.ProductDetails.as_view(), name='product_details'),

]
