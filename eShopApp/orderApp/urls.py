from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products", views.products, name="products"),
    path("products/<int:id>", views.productsDetails, name="productsDetails"),
    path("products/create", views.create_product, name="productsCreate"),
    path("orders", views.orders, name="orders"),
    path("about", views.about, name="about"),


]