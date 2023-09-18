from django.shortcuts import render

from dws_site.models import Dws

from dws_site.models import Category


# Create your views here.

def home_page(request):
    if request.method == "GET":
        data = {"dwses": Dws.objects.all(), "categories": Category.objects.all()}
        return render(request, "index.html", context=data)


def show_goods_category(request, category_slug):
    if request.method == "GET":
        category = Category.objects.get(slug=category_slug)
        data = {"dwses": category.goods.all(), "categories": Category.objects.all()}
        return render(request, "index.html", context=data)


def detail_good(request, category_slug, dws_slug, dws_id):
    if request.method == "GET":
        data = {"categories": Category.objects.all(), "dws_item": Dws.objects.get(id=dws_id)}
        return render(request, "detail_good.html", context=data)


def payment(request):
    return render(request, "payment.html")


def about_us(request):
    return render(request, "about_us.html")


def delivery(request):
    return render(request, "delivery.html")
