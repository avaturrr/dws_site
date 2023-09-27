from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
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
    created_at = models.DateTimeField(verbose_name="время создания", auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT,
                                related_name="profils", verbose_name="пользователь")

    def __str__(self):
        return self.company_name
