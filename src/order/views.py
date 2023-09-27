from django.http import HttpResponse
from django.shortcuts import render, redirect

from order.forms import OrderForm

from cart.cart import Cart

from order.models import Order, OrderItem

from login_out_reg.models import Profile


# Create your views here.
def create_order(request):
    cart = Cart(request)
    if request.method == "GET":
        if len(cart) != 0:
            try: #если у пользователя нет профиля, передастся нон
                used_profile = Profile.objects.get(user=request.user)
            except TypeError:
                used_profile = None

            form_for_order = OrderForm(used_profile)
            return render(request, "create_order.html", context={"form_for_order": form_for_order})
        else:
            return HttpResponse("Корзина пуста! Добавьте товары")
    else:
        try: #если у пользователя нет профиля, передастся нон
            used_profile = Profile.objects.get(user=request.user)
        except TypeError:
            used_profile = None
        form_for_order = OrderForm(used_profile, request.POST)
        if form_for_order.is_valid():
            data_for_save = form_for_order.save(commit=False)
            try: #если у пользователя нет профиля, поле будет пустым
                data_for_save.profile = used_profile
            except AttributeError:
                pass
            data_for_save.save()

        # if form_for_order.is_valid():
        #     cd = form_for_order.cleaned_data
        #     order = Order.objects.create(company_name=cd["company_name"],
        #                                  company_tax_id=cd["company_tax_id"],
        #                                  legal_adress=cd["legal_adress"], post_adress=cd["post_adress"],
        #                                  company_email=cd["company_email"], phone_number=cd["phone_number"],
        #                                  delivery_adress=cd["delivery_adress"], position=cd["position"],
        #                                  position_name=cd["position_name"], bank_details=cd["bank_details"],
        #                                  comments=cd["comments"])
        #     for item in cart:
        #         OrderItem.objects.create(order=order, product=item["product"],
        #                                  price=item["price"], quantity=item["quantity"],
        #                                  total_sum=item["total_price"])
            cart.clean_cart()
        return redirect("home_page")
