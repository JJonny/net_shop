from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    return render(request, "home.html",
                    {'category': Category.objects.all(),
                     'products': Product.objects.all() })


def tea_category(request, category_id):
    tea_list = Product.objects.filter(prod_category=category_id)
    return render(request, "tea.html", {'category': Category.objects.all(),
                                        'tea_list': tea_list})


def tea_description(request, slug):
    tea = get_object_or_404(Product, prod_slug=slug)
    return render(request, "tea-description.html", {'category': Category.objects.all(),
                                        'tea': tea})
                                        
                                        
def about(request):
    return render(request, 'about.html', {'category': Category.objects.all()})
                                        
                                        
                                        