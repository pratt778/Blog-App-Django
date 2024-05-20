from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    cid= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    desc=models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='category/')

    def img_show(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"/>'.format(self.image))

    def __str__(self):
        return self.name

class Post(models.Model):
    pid= models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=HTMLField()
    url=models.CharField(max_length=200)
    img = models.ImageField(upload_to='post/')
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
    date = models.DateTimeField(auto_now_add=True)

    def img_show(self):
        return format_html('<img src="/media/{}" style="width=40px;height:40px;border-radius:50%;"/>'.format(self.img))

    def __str__(self):
        return self.title
    
