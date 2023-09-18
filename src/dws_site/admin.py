from django.contrib import admin

from dws_site.models import Dws, Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class DwsAdmin(admin.ModelAdmin):
    list_display = ("goods_name", "goods_id", "price")
    prepopulated_fields = {"slug": ("goods_name",)}


admin.site.register(Dws, DwsAdmin)
admin.site.register(Category, CategoryAdmin)
