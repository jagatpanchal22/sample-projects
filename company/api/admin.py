from django.contrib import admin
from .models import Order, Company


# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = "order_date"
    list_display = (
        "id",
        "summary",
        "order_date",
        "order_by",
        "managed_by",
        "status",
    )
    list_filter = ("order_by", "managed_by")


admin.site.register(Company)
admin.site.register(Order, OrderAdmin)
