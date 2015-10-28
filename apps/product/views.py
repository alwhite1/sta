import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.views import login_required
from .models import Product, Category

def main(request):
    return redirect(get_categories(request))

def get_categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def get_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category_id=category.id)
    return render(request, 'category.html', {'products': products, 'category': category})


def get_product(request, double_slug):
    product_slug = double_slug.split('/')[1]
    product = Product.objects.get(slug=product_slug)
    category__slug = double_slug.split('/')[0]
    return render(request, 'product.html', {'product': product, 'product_slug': product_slug,
                                            'category_slug': category__slug})

@login_required
def get_last(request):
    data_time_delta = datetime.datetime.now() - datetime.timedelta(days=1)
    products = Product.objects.filter(created_at__gt=data_time_delta)
    return render(request, 'last.html', {'products': products})
