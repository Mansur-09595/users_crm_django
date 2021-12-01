from django.urls import path
from .views import HomePostView, DeletePostView, CreatePostView, UpdatePostView, DetailPostView, CreateGategoryView, CatListView, CreateCommentView, CreateLanguageView, LangListView

urlpatterns = [
    path(r'', HomePostView.as_view(), name="home"),
    path(r'<int:pk>', DetailPostView.as_view(), name="article_detail"),
    path(r'add_post/', CreatePostView.as_view(), name="add_post"),

    path(r'add_category/', CreateGategoryView.as_view(), name="add_category"),
    path(r'add_language/', CreateLanguageView.as_view(), name="add_language"),


    path(r'<int:pk>/edit/', UpdatePostView.as_view(), name="update_post"),
    path(r'<int:pk>/delete/', DeletePostView.as_view(), name="delete_post"),

    path(r'category/<category>/', CatListView.as_view(), name="category"),
    path(r'language/<language>/', LangListView.as_view(), name="language"),


    path(r'article/<int:pk>/comment/', CreateCommentView.as_view(), name="add_comment"),
]