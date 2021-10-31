from django import forms
from .models import Post, Category

# choices = Category.objects.all().values_list('name', 'name')

# choice_list = []

# for item in choices:
#     choice_list.append(item)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'images', 'category', 'body',)

        # widgets = {
        #     'category': forms.Select(choices=choice_list, attrs={'class': 'form-group'})
        # }