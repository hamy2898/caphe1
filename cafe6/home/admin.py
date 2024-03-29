from django.contrib import admin
from .models import Category,Product

# Register your models here.
class CateAdmin(admin.ModelAdmin):
    list_display = ('title','id','description')

    class Meta:
        model = Category

admin.site.register(Category, CateAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','category','product_img','price')

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

