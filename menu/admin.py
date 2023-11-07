from django.contrib import admin
from .models import MenuItem, Table, Order, OrderItem
# Register your models here.

admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(OrderItem)