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
