from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Products
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return HttpResponse("Hello world")


def products(request):
    page_obj = products = Products.objects.all()

    product_name = request.GET.get('product_name')
    if product_name!='' and product_name is not None:
        page_obj = products.filter(name__icontains=product_name)

    paginator = Paginator(page_obj,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={
        'page_obj' : page_obj
    }
    return render(request, 'myapp/index.html', context)

#class based listview
class ProductListView(ListView):
    model = Products
    template_name = 'myapp/index.html'
    context_object_name = 'products'
    paginate_by = 3


def product_detail(request,id):
    product = Products.objects.get(id=id)
    context={
        'product' : product
    }
    return render(request, 'myapp/detail.html', context)

#class based detail view
class ProductDetailView(DetailView):
    model = Products
    template_name = 'myapp/detail.html'
    context_object_name = 'product'


@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        seller_name = request.user
        product = Products(name=name,price=price, desc=desc, image=image, seller_name = seller_name)
        product.save()


    return render(request, 'myapp/addproduct.html')

#class based view for create product
class ProductCreateView(CreateView):
    model = Products
    fields = ['name', 'price', 'desc', 'image', 'seller_name']

    success_url = reverse_lazy('myapp:products')
    
    
    #product_form.html


# def update_product(request,id):
#     product = Products.objects.get(id=id)

#     if request.method == 'POST':
#         product.name = request.POST.get('name')
#         product.price = request.POST.get('price')
#         product.desc = request.POST.get('desc')
#         product.image = request.FILES['upload']
#         product.save()
#         return redirect('/myapp/products')

#     context={
#         'product' : product
#     }
#     return render(request, 'myapp/updateproduct.html',context)

class ProductUpdateView(UpdateView):
    model = Products
    fields = ['name', 'price', 'desc', 'image', 'seller_name']
    template_name_suffix = '_update_form'

def delete_product(request, id):
    product = Products.objects.get(id=id)
    context={
        'product' : product,
    }

    if request.method == 'POST':
        product.delete()
        return redirect('/myapp/products')
    
    return render(request,'myapp/delete.html', context)

#class based deleteview
class ProductDelete(DeleteView):
    model = Products
    success_url = reverse_lazy('myapp:products')


def my_listings(request):
    products = Products.objects.filter(seller_name=request.user)
    context = {
        'products' : products,
    }
    return render(request, 'myapp/mylistings.html',context)

