from django.shortcuts import render
from django.core.serializers import serialize

from django.http import HttpResponse

from .models import Product

def home(request):
    return render(request, "pages/home.html", {})

def products(request):
    products = Product.objects.all()

    
    # Serializing the product object to JSON
    product_json = serialize('json', products)

    return render(request, "pages/productsList.html", {"products": products, "jsonprd": product_json})

def orders(request):
    return render(request, "pages/orders.html", {})

def about(request):
    return render(request, "pages/about.html", {})
