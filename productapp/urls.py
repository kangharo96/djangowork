from django.urls import path

from productapp import views
app_name = 'productapp'

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    # path('<pk>/delete/', views.ProductDelete.as_view()),
]
