from django.shortcuts import render
from .models import MenuItem, Order, OrderItem, Table
# Create your views here.
def all_items(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu/all_items.html', {'menu_items': menu_items})