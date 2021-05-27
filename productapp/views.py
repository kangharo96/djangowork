from django.contrib import auth
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from productapp.models import Product, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from productapp.forms import ProductForm


# Create your views here.
class CategoryList(ListView):
    model = Category
    pass


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
    context_object_name = 'product'


def product_new(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.save()
            return HttpResponseRedirect(reverse('productapp:product_detail', args=(prod.pk,)))
    else:
        form = ProductForm()
        return render(request, 'productapp/product_new.html', {'form': form})


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'category', 'description', 'price', 'image']
    template_name = 'productapp/product_new.html'
    success_url = reverse_lazy('productapp:product_list')


class ProductEdit(UpdateView):
    model = Product
    template_name = 'productapp/product_edit.html'
    fields = ['name', 'description', 'price', 'image']
    success_url = reverse_lazy('productapp:product_list')


class ProductDelete(DeleteView):
    model = Product
    template_name = 'productapp/product_delete.html'
    success_url = reverse_lazy('productapp:product_list')

