from django.shortcuts import render, redirect

from cart.cart import Cart

from dws_site.models import Product

from cart.forms import CartAddProductForm


# Create your views here.

def cart_detail(request):
    if request.method == "GET":
        cart = Cart(request)  # cart итерируемый объект
        total_sum = 0
        len_cart = 0
        for i in cart:
            total_sum += i["total_price"]
            len_cart += 1
        data = {"cart": cart, "total_sum": total_sum, "len_cart": len_cart}
        return render(request, "cart_detail.html", context=data)


def cart_add(request, product_id):
    if request.method == "POST":
        cart = Cart(request)  # создаем объект класса Cart. Там либо пустой словарь, либо полный
        product = Product.objects.get(id=product_id)  # получаем объект, который добавляем в корзину
        cart_product_form = CartAddProductForm(request.POST)  # получаем данные с ПОСТ с формы
        if cart_product_form.is_valid():  # проверка валидации формы
            cd = cart_product_form.cleaned_data  # возврачает очищеный словарь из формы
            cart.add(product=product,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])  # вызывает метод класса Cart по добавлению товара
        return redirect('home_page')


def product_delete(request, product_id):
    if request.method == "GET":
        cart = Cart(request)
        cart.delete(str(product_id))
    return redirect("cart_detail")
