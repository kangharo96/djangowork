from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from productapp.models import Product

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
class ProductList(ListView):
    # latest_products = Product.objects.all()
    # context = {'latest_products': latest_products}
    # return render(request, 'productapp/index.html', context)
    template_name = 'productapp/product_list.html'
    model = Product
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    template_name = 'productapp/product_detail.html'


# def create(request):
#     pass
#
#
# class ProductDelete(DeleteView):
#     model = Product
#     success_url = '/'

