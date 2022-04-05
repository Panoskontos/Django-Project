from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    
    path('',watch),
    path('test/',test, name='test'),
    path('example/',example, name='example'),
    path('product/<str:name>',product, name='product'),
    path('create_new_product',create_new_product, name='create_new_product'),
    path('update_product/<str:pk>',update_product, name='update_product'),
    path('delete_product/<str:pk>',delete_product, name='delete_product'),
    path('success/<str:message>',success, name='success'),
    
    
    path('category/<str:category>/',product_by_category, name="product_by_category"),
    path('import/', ImportDocument, name="import"),

    # Class Based Views
    path('reviews/', ReviewList.as_view(),name="reviews"),
    path('reviews/<str:pk>', ReviewDetail.as_view(),name="review-object"),
    path('create_review', ReviewCreate.as_view(),name="create-review"),
    path('update_review/<str:pk>', ReviewUpdate.as_view(),name="create-review"),
    path('delete_review/<str:pk>', ReviewDelete.as_view(),name="delete-review"),
]
