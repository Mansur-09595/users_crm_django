from django.urls import path
from .views import UserRegisterView, ArticleListView

urlpatterns = [
    path(r'', ArticleListView.as_view(), name='home'),
    path(r'register/', UserRegisterView.as_view(), name='register')
]