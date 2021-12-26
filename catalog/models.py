from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField("Название", max_length=256)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField('Название', max_length=256)
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2)
    description = models.TextField('Описание')
    category = models.ForeignKey(Category, verbose_name='Категории', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    image = models.ImageField('Изображение', upload_to='imgs/')
    product = models.ForeignKey(Product, verbose_name='Картинка товара', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Картинка товара'
        verbose_name_plural = 'Картинка товаров'

    def __str__(self):
        return self.image.name