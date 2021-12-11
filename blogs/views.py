from rest_framework import generics

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Category
from .serializers import UsersSerializer
from .forms import PostForm

#Home_Page_View
class HomePostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomePostView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context


class DetailPostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'article_detail.html'

#Create_Post_View
class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#Create_Category_view
class CreateGategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add_category.html'

#Update_View
class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

#Delete_View
class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

#Category_Choise_View
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

# API_VIEWS
class UsersApiList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = UsersSerializer

class UsersApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = UsersSerializer