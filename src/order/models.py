from django.db import models

from dws_site.models import Product

from login_out_reg.models import Profile


# Create your models here.

class Order(models.Model):
    company_name = models.CharField(verbose_name="название организации")
    company_tax_id = models.CharField(verbose_name="УНП")
    legal_adress = models.TextField(verbose_name="юридический адрес")
    post_adress = models.TextField(verbose_name="почтовый адрес")
    company_email = models.EmailField(verbose_name="эл адрес")
    phone_number = models.CharField(null=True, verbose_name="телефон для связи")
    delivery_adress = models.TextField(verbose_name="адрес доставки")
    position = models.CharField(verbose_name="должность для договора")
    position_name = models.CharField(verbose_name="ФИО для договора")
    bank_details = models.CharField(verbose_name="банковские реквизиты")
    comments = models.TextField(verbose_name="комментарии к заказу")
    created_at = models.DateTimeField(verbose_name="время создания", auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name="orders", null=True)

    def __str__(self):
        return self.company_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              verbose_name="заказ", related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT,
                                   verbose_name="товар", related_name="items")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="цена")
    quantity = models.IntegerField(verbose_name="количество")
    total_sum = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="общая стоимость")

    def __str__(self):
        return self.order.company_name
