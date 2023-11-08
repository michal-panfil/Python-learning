from django.shortcuts import get_object_or_404, render
from django.core.serializers import serialize

from django.http import HttpResponse
from flask import redirect

from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, "pages/home.html", {})

def products(request):
    products = Product.objects.all()
    return render(request, "pages/productsList.html", {"products": products})

def productsDetails(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "pages/productDetails.html", {"product": product})

def productsCreate(request):
    return render(request, "pages/productCreate.html", {})

def orders(request):
    return render(request, "pages/orders.html", {})

def about(request):
    return render(request, "pages/about.html", {})



def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')  # Assuming you have a url named 'product_list' to redirect to
    else:
        form = ProductForm()
    return render(request, 'pages/productCreate.html', {'form': form})