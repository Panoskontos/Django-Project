from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *



def home(request):
    # Python logic

    # Data
    context = {
        # "products": products
    }

    # Which html you want to link
    return render(request, 'index.html', context)





def watch(request):
    context = {
    }
    return render(request, 'myapp/index.html', context)

# Categiries
def test(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'myapp/test.html', context)


# Products
def example(request):
    products = Product.objects.all()
    print(products)
    context = {
        'products':products
    }
    return render(request, 'myapp/example.html',context)

# def get_category_products(request,pk):
