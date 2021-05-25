from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from productapp.models import Product


# Create your views here.
def index(request):
    latest_products = Product.objects.all()
    context = {'latest_products': latest_products}
    return render(request, 'productapp/index.html', context)


def detail(request, product_id):
    product_item = get_object_or_404(Product, pk=product_id)
    return render(request, 'productapp/detail.html', {'product': product_item})

