from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
# Create your views here.
def index(request):
    return HttpResponse("Hello world")


def products(request):
    products = Products.objects.all()
    context ={
        'products': products
    }
    return render(request, 'myapp/index.html', context)

def product_detail(request,id):
    product = Products.objects.get(id=id)
    context={
        'product' : product
    }
    return render(request, 'myapp/detail.html', context)
