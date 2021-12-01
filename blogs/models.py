from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

#Create category models
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя отдела')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

#Create language models
class Language(models.Model):
    name = models.CharField(max_length=255, verbose_name='Язык')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

#Create users models
class Post(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    age = models.IntegerField(default=0, verbose_name='Возраст')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1, max_length=255, verbose_name='Отдел')
    language = models.ForeignKey(Language, on_delete=models.PROTECT, default=1, max_length=255, verbose_name='Язык программирование')
    post_date = models.DateField(auto_now_add=True,)

    def __str__(self):
        return self.first_name + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')

#Create сomment models
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    def get_absolute_url(self):
        return reverse('add_comment')