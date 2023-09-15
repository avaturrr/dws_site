# Create your models here.
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Dws(models.Model):
    class Meta:
        verbose_name = "двигатель"
        verbose_name_plural = "двигатели"

    goods_name = models.CharField(verbose_name="название двигателя")
    goods_id = models.IntegerField(verbose_name="артикул")
    manufacturer = models.CharField(verbose_name="производитель")
    transport_model = models.CharField(verbose_name="применяемость")
    category = models.CharField(verbose_name="категория")
    price = models.FloatField(verbose_name="цена")
    image = models.ImageField(verbose_name="фото")

    def __str__(self):
        return self.goods_name

# Create your models here.
