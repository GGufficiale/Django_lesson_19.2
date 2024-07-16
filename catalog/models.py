from django.db import models

"""Создание модели для БД с объектами каталога"""
NULLABLE = {'blank': True, 'null': True}  # форма, если параметр необязателен


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=1000, verbose_name='описание')
    # Сразу после внесения изменений в модель создаем миграцию"""
    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'штука'
        verbose_name_plural = 'штуки'
        ordering = ['name', 'description']


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=1000, verbose_name='описание')
    photo = models.ImageField(upload_to='catalog/photo', verbose_name="фото товара", **NULLABLE)
    # Для работы с изображениями в Джанго надо не забыть установить пакет Pillow"""
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, verbose_name='категория', **NULLABLE,
                                 related_name="product")
    # При связи продукта и категории (ForeignKey) не забыть добавить 'to'."""
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateField(**NULLABLE, verbose_name='дата создания записи в БД', auto_now_add=True)
    updated_at = models.DateField(**NULLABLE, verbose_name='дата последнего изменения записи в БД', auto_now=True)
    manufactured_at = models.DateField(**NULLABLE, verbose_name='дата производства продукта')

    # Сразу после внесения изменений в модель создаем миграцию"""

    def __str__(self):
        return f'{self.name}: {self.description}. Цена: {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name', 'description', 'price']
