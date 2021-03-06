"""inventory_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from inventory_app import settings
from productapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('productapp.urls', namespace='productapp')),
    path('', TemplateView.as_view(template_name='base.html')),
    path('login/', auth_views.LoginView.as_view(template_name='productapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='productapp:product_list'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#inventory_app is project
