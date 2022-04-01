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
    # για ολα βαζεις all()
    products = Product.objects.all()
#  για 1 βαζεις get()
    one_product = Product.objects.get(name="Laptop")

    # για συγκεκριμενη ομαδα βαζεις .filter()
    # lte = lower than equal
    # gte = greater than equal
    # cheap_products = Product.objects.all().filter(price__lte=100)
    # cheap_products = Product.objects.all().filter(name__icontains="r")
    cheap_products = Product.objects.filter(date_created__hour=18)

    context = {
        'products':products,
        'one_product':one_product,
        'cheap_products':cheap_products,
    }
    return render(request, 'myapp/example.html',context)



# asdasdasdasdasd
# asdasdasdasdasd
# sadasdasdasdasd
# asdasdasdasdasd


products = [
    {'id':1, 
    'name':"laptop",
    'price':900,
    "category":{'name':'Electronics','id':40}}
]

# products.category