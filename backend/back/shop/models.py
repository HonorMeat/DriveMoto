from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=255, verbose_name='Название продукта')
    cost = models.IntegerField(verbose_name='Цена')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Категория продукта')
    amount = models.IntegerField(verbose_name='Количество товара на складе')
    discountPrice = models.IntegerField(verbose_name='Цена со скидкой', blank=True, null=True)
    dateSold = models.DateTimeField(verbose_name='Дата окончания акции')
    
    def __str__(self):
        return self.title

class Watercraft(Product):
    madiIn = models.CharField(max_length=255, verbose_name='Страна производителя')
    place = models.IntegerField(verbose_name='Количество мест')
    power = models.IntegerField(verbose_name='Мощность') 