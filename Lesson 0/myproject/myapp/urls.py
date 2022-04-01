from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    
    path('',watch),
    path('test/',test, name='test'),
    path('example/',example, name='example'),
]
