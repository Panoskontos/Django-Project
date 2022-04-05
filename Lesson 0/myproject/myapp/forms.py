from django.forms import ModelForm

from .models import Product, Review, Document

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'