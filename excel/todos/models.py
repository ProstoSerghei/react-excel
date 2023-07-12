from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, models.PROTECT, verbose_name='Пользователь')
    order = models.IntegerField(verbose_name='Номер заказа')
    title = models.CharField(max_length=128, default='', verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    state = models.BooleanField(default=False, verbose_name='Состояние')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    created = models.DateTimeField(auto_now=True, verbose_name='Посл. обновление')
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self) -> str:
        return f'{self.title}'