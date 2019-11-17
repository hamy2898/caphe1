from django.db import models
from django.utils import timezone


# Create your models here.

#Product
class Category(models.Model):
    title = models.CharField(max_length=100,default='')
    description = models.TextField(default='')
    active = models.BooleanField(default=True)

class Product(models.Model):
    title = models.CharField(max_length=255,default='')
    description = models.TextField(default='')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_img = models.CharField(max_length=255,default='')
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,default='')
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    investory = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

class BaiViet(models.Model):
    baiviet_id = models.IntegerField(auto_created=True, primary_key=True)
    tieude = models.CharField(max_length=300)
    noidung = models.TextField()
    ngay_dang = models.DateTimeField(default=timezone.now)
    anhbia = models.CharField(max_length=300)

class CartItem(models.Model):
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_amount_saved(self):
        return self.get_total_item_price()


class Cart(models.Model):
    cart_id = models.IntegerField(auto_created=True, primary_key=True)
    items = models.ManyToManyField(CartItem)
    ordered_date = models.DateTimeField(default=timezone.now)
    ordered = models.BooleanField(default=False)
    def get_total(self):
        total = 0
        for cart_item in self.items.all():
            total += cart_item.get_final_price()
            return total






