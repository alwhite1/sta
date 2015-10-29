import datetime
from django.shortcuts import render
from django.contrib.auth.views import login_required
from .models import Product, Category


def main(request):
    return render(request, 'main.html')


def get_categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def get_category(request, category_slug):
    single_category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=single_category)
    return render(request, 'category.html', {'products': products, 'category': single_category})


def get_product(request, double_slug):
    product_slug = double_slug.split('/')[1]
    product = Product.objects.get(slug=product_slug)
    return_url = request.META.get('HTTP_REFERER', '/')
    return render(request, 'product.html', {'product': product, 'return_url': return_url})


@login_required
def get_last(request):
    data_time_delta = datetime.datetime.now() - datetime.timedelta(days=1)
    products = Product.objects.filter(created_at__gt=data_time_delta)
    return render(request, 'last.html', {'products': products})
