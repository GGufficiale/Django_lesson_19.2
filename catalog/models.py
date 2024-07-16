from django.db import models

"""Создаем модель для БД с объектами каталога"""
NULLABLE = {'blank': True, 'null': True}  # форма, если параметр необязателен


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=1000, verbose_name='описание')
    price = models.IntegerField(max_length=10000, verbose_name='цена')
    photo = models.ImageField(upload_to='catalog/photo', verbose_name="фото товара", **NULLABLE)
    """Для работы с изображениями в Джанго надо не забыть установить пакет Pillow"""

    is_active = models.BooleanField(default=True, verbose_name='учится')
    """Сразу после внесения изменений в модель создаем миграцию"""

    def __str__(self):
        return f'{self.name}: {self.description}. Цена: {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['price', 'name']


class Category(Product, models.Model):
    def __init__(self, name, description, price, photo):
        super().__init__(name, description, price, photo)

    model = models.CharField(max_length=100, verbose_name='тип')
    colour = models.CharField(max_length=1000, verbose_name='цвет')

    is_active = models.BooleanField(default=True, verbose_name='учится')
    """Сразу после внесения изменений в модель создаем миграцию"""

    def __str__(self):
        return f'{self.name}: {self.description}. Цена: {self.price}. Тип: {self.model}, цвет: {self.colour}'

    class Meta:
        verbose_name = 'штука'
        verbose_name_plural = 'штуки'
        ordering = ['price', 'name', 'model']
