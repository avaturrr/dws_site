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
    cat = models.ForeignKey("Category", on_delete=models.PROTECT,
                                 verbose_name="категория", related_name="goods")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="цена")
    image = models.ImageField(verbose_name="фото")

    def __str__(self):
        return self.goods_name


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField(max_length=100, db_index=True, verbose_name="Название категории")
    slug = models.SlugField(max_length=225, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name
