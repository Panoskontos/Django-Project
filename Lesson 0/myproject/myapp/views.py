from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

products = [
    {'id': 1, 'name': 'watch', 'price': 100},
    {'id': 2, 'name': 'hoodie', 'price': 40},
]


def home(request):
    # Python logic

    # Data
    context = {
        "products": products
    }

    # Which html you want to link
    return render(request, 'index.html', context)


def watch(request):
    context = {
    }
    return render(request, 'myapp/index.html', context)

def test(request):
    context = {
    }
    return render(request, 'myapp/test.html', context)


def example(request):
    context = {}
    return render(request, 'myapp/example.html',context)

