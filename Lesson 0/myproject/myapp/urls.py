from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    
    path('',watch),
    path('test/',test, name='test'),
    path('example/',example, name='example'),
    path('product/<str:name>',product, name='product'),
    path('create_new_product',create_new_product, name='create_new_product'),
    path('category/<str:category>/',product_by_category, name="product_by_category")
]
