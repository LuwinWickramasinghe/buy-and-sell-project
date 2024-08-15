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

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        product = Products(name=name,price=price, desc=desc, image=image)
        product.save()


    return render(request, 'myapp/addproduct.html')

def update_product(request,id):
    product = Products.objects.get(id=id)
    context={
        'product' : product
    }
    return render(request, 'myapp/updateproduct.html',context)