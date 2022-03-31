from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # Python logic

    # Data
    context = {}

    # Which html you want to link
    return render(request, 'index.html', context)


def watch(request):
    return HttpResponse('watch')
