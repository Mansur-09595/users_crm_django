from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

#Create category models
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя парковки')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

#Create users models
class Post(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Имя и Фамилия')
    time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Время')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1, max_length=255, verbose_name='Отдел')
    # language = models.ForeignKey(Language, on_delete=models.PROTECT, default=1, max_length=255, verbose_name='Язык программирование')
    post_date = models.DateField(auto_now_add=True,)

    def __str__(self):
        return self.full_name + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')