from django.db import models

"""Создаем модель для БД со студентами"""
NULLABLE = {'blank': True, 'null': True}


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    avatar = models.ImageField(upload_to='students/', verbose_name="аватар", **NULLABLE)
    """Для работы с изображениями в Джанго надо не забыть установить пакет Pillow"""

    is_active = models.BooleanField(default=True, verbose_name='учится')
    """Сразу после внесения изменений в модель создаем миграцию"""

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ('last_name',)
