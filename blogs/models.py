from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from datetime import datetime, date

from django_resized import ResizedImageField

from django.contrib.auth import get_user_model

#Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя раздела')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Загаловок')
    images = ResizedImageField(size=[320, 320], crop=['middle', 'center'], null=True, blank=True, 
                               unique=True, upload_to="images/", verbose_name='Фото')
    slug = models.SlugField(unique=True, null=False, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    body = models.TextField(verbose_name='Текст')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1, max_length=255, verbose_name='Раздел')
    post_date = models.DateField(auto_now_add=True,)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

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