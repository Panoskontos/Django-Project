from tkinter import CASCADE
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
     return self.name

class Product(models.Model):
    name =models.CharField(max_length=100)
    price = models.FloatField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
     return self.name


class Review(models.Model):
    username = models.CharField(max_length=100)
    text = models.TextField(blank=True,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
     return self.text

class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(blank=True, null=True)