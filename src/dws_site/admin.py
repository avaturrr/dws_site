from django.contrib import admin

from dws_site.models import Product, Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_art", "price")
    prepopulated_fields = {"slug": ("product_name",)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
