from django.contrib import admin


from .models import Product, Profile, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug" : ("name",)}

admin.site.register(Category, CategoryAdmin)

admin.site.register(Profile)


class ProductAdmin(admin.ModelAdmin):


    list_display = ('category', 'model', 'cost',)
    prepopulated_fields = {"slug" : ("category", "model")}
admin.site.register(Product, ProductAdmin)
