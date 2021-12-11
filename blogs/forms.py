from django import forms
from .models import Post


#Форма отображения таблицы 
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('full_name', 'time',  'category', )