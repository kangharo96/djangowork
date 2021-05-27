from django.urls import path

from productapp import views
app_name = 'productapp'

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),  # 127.0.0.1:8000/products
    path(r'<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),  # 127.0.0.1:8000/products/pk
    path(r'<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),  # 127.0.0.1:8000/products/pk/delete
    path(r'new/', views.ProductCreate.as_view(), name='product_new'),  # 127.0.0.1:8000/products/new
    path(r'<int:pk>/edit/', views.ProductEdit.as_view(), name='product_edit'),
]
