from django.contrib import admin
from .models import Category,Post
# Register your models here.

class CategoryDisplay(admin.ModelAdmin):
    list_display=('cid','name','url','desc','image','date')


class PostDisplay(admin.ModelAdmin):
    list_display=('pid','title','content','url','img','cat','date')


admin.site.register(Category,CategoryDisplay)
admin.site.register(Post,PostDisplay)


