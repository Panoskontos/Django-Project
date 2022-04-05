from django.forms import ModelForm

from .models import Product, Review

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'