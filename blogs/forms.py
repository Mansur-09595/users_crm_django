from django import forms
from .models import Comment, Post


#Форма отображения таблицы 
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('first_name', 'last_name', 'age', 'category', 'language', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-group'}),
            'body': forms.TextInput(attrs={'class': 'form-group'}),
        }