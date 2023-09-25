from django.contrib import admin

# Register your models here.
from django.contrib import admin

from order.models import OrderItem, Order


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ("company_name", "company_tax_id", "created_at")


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "price", "quantity", "total_sum")


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
