from django.shortcuts import render

from dws_site.models import Product

from dws_site.models import Category

from cart.forms import CartAddProductForm


# Create your views here.

def home_page(request):
    if request.method == "GET":
        cart_product_form = CartAddProductForm()
        data = {"products": Product.objects.all(), "categories": Category.objects.all(),
                "cart_product_form": cart_product_form}
        return render(request, "index.html", context=data)


def show_product_category(request, category_slug):
    if request.method == "GET":
        category = Category.objects.get(slug=category_slug)
        data = {"products": category.products.all(), "categories": Category.objects.all()}
        return render(request, "index.html", context=data)


def detail_product(request, category_slug, product_slug, product_id):
    if request.method == "GET":
        cart_product_form = CartAddProductForm()
        data = {"categories": Category.objects.all(),
                "product_item": Product.objects.get(id=product_id),
                "cart_product_form": cart_product_form}
        return render(request, "detail_product.html", context=data)


def payment(request):
    return render(request, "payment.html")


def about_us(request):
    return render(request, "about_us.html")


def delivery(request):
    return render(request, "delivery.html")
