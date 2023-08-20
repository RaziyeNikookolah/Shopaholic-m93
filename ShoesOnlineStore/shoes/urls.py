from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.ProductList.as_view(), name='product_list'),
    #     path('search_list/',
    #          views.ProductSearchListView.as_view(), name='search_list'),
    #     path('product_update/<int:pk>/',
    #          views.ProductUpdate.as_view(), name='product_update'),
]
