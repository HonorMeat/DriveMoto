from django.contrib import admin
from .models import Product, Category, Sale

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'category', 'amount')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('dateSold', 'price', 'productSale')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sale, SaleAdmin)