from django.contrib import admin
from .models import Category,Post
# Register your models here.

class CategoryDisplay(admin.ModelAdmin):
    list_display=('img_show','cid','name','url','desc','date')
    search_fields=('name',)
    list_per_page=15


class PostDisplay(admin.ModelAdmin):
    list_display=('img_show','pid','title','url','cat','date')

    search_fields=('title',)

    list_filter=('cat',)
    list_per_page=15


admin.site.register(Category,CategoryDisplay)
admin.site.register(Post,PostDisplay)


