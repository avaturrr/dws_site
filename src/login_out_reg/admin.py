from django.contrib import admin

from login_out_reg.models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("company_name", "company_tax_id", "created_at")


admin.site.register(Profile, ProfileAdmin)
