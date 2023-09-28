import datetime
import os

from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from order.forms import OrderForm

from cart.cart import Cart

from login_out_reg.models import Profile

from src.settings import EMAIL_HOST_USER

from docxtpl import DocxTemplate

from order.models import OrderItem


# Create your views here.
def create_order(request):
    cart = Cart(request)
    if request.method == "GET":
        now = datetime.datetime.now()
        hour_now = now.hour
        if 7 < hour_now < 19:
            if len(cart) != 0:
                try:
                    used_profile = Profile.objects.get(user=request.user)
                except ObjectDoesNotExist:
                    used_profile = None
                except TypeError:
                    used_profile = None

                form_for_order = OrderForm(used_profile)
                return render(request, "create_order.html", context={"form_for_order": form_for_order})
            else:
                return HttpResponse("Корзина пуста! Добавьте товары")
        else:
            return HttpResponse("Невозможно сделать заказ. Заказы принимаются с 7.00 по 19.00")
    else:
        try:  # если у пользователя нет профиля или нет пользователя, поле будет пустым
            used_profile = Profile.objects.get(user=request.user)
        except ObjectDoesNotExist:
            used_profile = None
        except TypeError:
            used_profile = None
        form_for_order = OrderForm(used_profile, request.POST)
        if form_for_order.is_valid():
            data_for_save = form_for_order.save(commit=False)
            try:  # если у пользователя нет профиля или нет пользователя, поле будет пустым
                data_for_save.profile = used_profile
            except AttributeError:
                pass
            data_for_save.save()
            for item in cart:
                OrderItem.objects.create(order=data_for_save, product=item["product"],
                                         price=item["price"], quantity=item["quantity"],
                                         total_sum=item["total_price"])
            cart.clean_cart()
        # заполнение файла
        doc = DocxTemplate("order/text_files/invoice_template.docx")
        context = {"company_name": data_for_save.company_name,
                   "company_tax_id": data_for_save.company_tax_id,
                   "legal_adress": data_for_save.legal_adress,
                   "post_adress": data_for_save.post_adress,
                   "delivery_adress": data_for_save.delivery_adress,
                   "position": data_for_save.position,
                   "position_name": data_for_save.position_name,
                   "bank_details": data_for_save.bank_details}
        doc.render(context=context)
        doc.save("invoice.docx")
        # отправление письма с подтверждением заказа
        email_to = data_for_save.company_email
        email = EmailMessage(subject="счет dws_site", body="счёт во вложении",
                             from_email=EMAIL_HOST_USER, to=[email_to, EMAIL_HOST_USER])
        email.attach_file("invoice.docx")
        email.send()
        # удаляем созданный из шаблона файл
        os.remove("invoice.docx")
        return redirect("home_page")

