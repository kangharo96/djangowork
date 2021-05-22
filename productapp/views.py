from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from productapp.models import Product


# Create your views here.
def product(request):
    return HttpResponse('You have reached the products page')


def index(request):
    return HttpResponse('You have reached the index')

