from django.shortcuts import render

from django.http import HttpResponse

from .models import Product

def home(request):
    return render(request, "pages/home.html", {})

def products(request):
    products = Product.objects.all()
    return render(request, "pages/productsList.html", {"products": products})

def orders(request):
    return render(request, "pages/orders.html", {})

def about(request):
    return render(request, "pages/about.html", {})
