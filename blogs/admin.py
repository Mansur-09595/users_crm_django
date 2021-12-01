from django.contrib import admin
from .models import Post, Category, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('first_name',)
    #prepopulated_fields = {'slug': ('first_name',)} # new


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)