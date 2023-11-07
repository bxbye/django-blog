from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu/', default='menu/tatli.jpg')

    def __str__(self) -> str:
        return self.name
    
class Table(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.table.name}'s Order"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT) # siparisten urun silinirse Menu'deki urun silinmeyecek.
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.item_total = self.menu_item.price * self.quantity
        super(OrderItem, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.menu_item.name} - Quantity: {self.quantity}"