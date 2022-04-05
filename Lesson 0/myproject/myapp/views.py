from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import *
from .forms import ProductForm, ReviewForm

# Class based Views
# Imports for class based views
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
# Redirecting
from django.urls import reverse_lazy


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
    # one_product = Product.objects.get(name="Laptop")

    # για συγκεκριμενη ομαδα βαζεις .filter()
    # lte = lower than equal
    # gte = greater than equal
    # cheap_products = Product.objects.all().filter(price__lte=100)
    # cheap_products = Product.objects.all().filter(name__icontains="r")
    cheap_products = Product.objects.filter(date_created__hour=18)

    context = {
        'products':products,
        # 'one_product':one_product,
        # 'cheap_products':cheap_products,
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


def product(request,name):
    # get 1 object
    
    product = Product.objects.get(name=name)
    
    context = {
        'product':product
    }
    return render(request, 'myapp/product.html', context)



def create_new_product(request):
    form = ProductForm()
    if request.method == 'POST':
        
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('example')
    context = {
        'form':form,
    }
    return render(request, 'myapp/form.html', context)


def update_product(request,pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            message = 'Item was updated with success'

            # Added at the end of class
            form.save()
            return redirect('success',message)
    context = {
        'form':form,
    }
    return render(request, 'myapp/form.html', context)


def delete_product(request, pk):
    # logic
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        


    # Versatility
    object = 'Laptop'
    context = {
        'object':object,
    }
    return render(request, 'myapp/delete.html', context)


def product_by_category(request,category):
    products = Product.objects.all()
    print(products)
    context = {
        'products':products,
        'category':category,
    }
    return render(request, 'myapp/product_by_category.html', context)

# Versatile Success
def success(request, message):
    return HttpResponse(str(message))
      

# Class Based Views
    # read
class ReviewList(ListView):
    # List
    model = Review
    context_object_name = 'reviews'
    # paginate_by = 10
    template_name = 'myapp/reviews.html'
    # you can search for other attributes to customize


class ReviewDetail(DetailView):
    # Detail
    model = Review
    context_object_name = 'review'
    template_name = 'myapp/review_object.html'



class ReviewCreate(CreateView):
    # Create
    model = Review
    # redirect
    success_url = reverse_lazy('reviews')
    form_class = ReviewForm
    template_name = 'myapp/create_review.html'

class ReviewUpdate(UpdateView):
    # Create
    model = Review
    # redirect
    success_url = reverse_lazy('reviews')
    form_class = ReviewForm
    template_name = 'myapp/create_review.html'

class ReviewDelete(DeleteView):
    # Create
    model = Review
    # redirect
    context_object_name = 'review'
    success_url = reverse_lazy('reviews')
    template_name = 'myapp/delete_review.html'