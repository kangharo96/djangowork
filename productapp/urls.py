from django.urls import path

from productapp import views
app_name = 'productapp'

urlpatterns = [
    path('', views.index, name='product'),
    path('<int:product_id>/', views.detail, name='detail'),
]
