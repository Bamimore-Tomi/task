from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.site_header = "Blog Admin"

class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'title','date_posted')
    list_fiter = ('author','date_posted',)

admin.site.register(Post, BlogAdmin)

 