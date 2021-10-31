from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Category
from .forms import PostForm

class HomePostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomePostView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

# def CategoryView(request, cats):
#     category_posts = Post.objects.filter(category=cats)
#     return render(request, 'categories.html', {'cats':cats, 'category_posts':category_posts})

class DetailPostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'article_detail.html'


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CreateGategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add_category.html'


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CatListView(ListView):
    context_object_name = 'catlist'
    template_name = 'category.html'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter()
        }
        return content

def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context