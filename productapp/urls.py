from django.urls import path

from productapp import views
app_name = 'productapp'

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path(r'<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path(r'<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
    path(r'new/', views.ProductCreate.as_view(), name='product_new'),
    path(r'<int:pk>/edit/', views.ProductEdit.as_view(), name='product_edit'),
]
