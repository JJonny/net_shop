from django.shortcuts import render
from .models import Product, Category


def home(request):
    return render(request, "home.html",
                    {'category': Category.objects.all(),
                     'products': Product.objects.all()})

