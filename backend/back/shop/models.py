from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model


    
class Category(models.Model):

    name = models.CharField(
        max_length=255,
        verbose_name='Название категории'
    )
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    # class Meta:
    #     abstract = True
    slug = models.SlugField()

    image = models.ImageField(
        upload_to='media/images/',
        height_field=None,
         width_field=None,
          max_length=100 
        )
    model = models.CharField(
        max_length=255, 
        verbose_name='Название подели'
    )
    cost = models.IntegerField(
        verbose_name='Цена'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE, 
        verbose_name='Категория продукта'
    )

    amount = models.IntegerField(
        verbose_name='Количество товара на складе',
        default=0
    )
    discountPrice = models.IntegerField(
        verbose_name='Цена со скидкой',
         blank=True, 
         null=True
        )
    dateSold = models.DateTimeField(
        verbose_name='Дата окончания акции',
        null=True,
        blank=True
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг',
        validators=[MinValueValidator(0),
        MaxValueValidator(5)]
    )
    made = models.DateField(
        verbose_name='Прозведено',
        null=True,
        blank=True
    )
    madeIn = models.CharField(
        max_length=255, 
        verbose_name='Страна производителя'
    )
    place = models.IntegerField(
        verbose_name='Количество мест', 
        null=True, 
        blank=True
    )
    power = models.IntegerField(
        verbose_name='Мощность', 
        null=True,
        blank=True
    )
    motor = models.CharField(
        max_length=255, 
        verbose_name='Тип двигателя',
        null=True,
        blank=True
    )

    weight = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        verbose_name='Вес'
    )
    
    color = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='Цвет'
    )
    empty = models.CharField(
        max_length=128,
        default='Закончилось',
        editable=False,
        null=True,
        blank=True

    )
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    def __str__(self):
        return '{}  {}'.format(self.category, self.model)

class Profile(models.Model):
    user = models.OneToOneField(
        to=get_user_model(),
        on_delete=models.CASCADE, 
        verbose_name="Пользватель"
    )
    izbrannye = models.ManyToManyField(
        Product,
        null=True,
        blank=True,
        verbose_name='Корзина'
    )
    avatar = models.ImageField(
        upload_to='media/avatar/',
        height_field=None, 
        width_field=None, 
        max_length=100
    )