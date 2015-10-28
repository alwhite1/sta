import datetime
from django.shortcuts import render
from .models import Product, Category


def get_categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def get_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return render(request, 'category.html', {'products': products})

def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product.html', {'product': product})

def get_last_product(request):
    data_time_delta = datetime.datetime.now() - datetime.timedelta(days=1)
    products = Product.objects.exclude(created_at>data_time_delta)
    return render(request, 'category.html', {'products': products})




