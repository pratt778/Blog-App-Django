from django.shortcuts import render
from .models import Post,Category
# Create your views here.
def home(request):
    Mypost = Post.objects.all()
    categories = Category.objects.all()
    data = {
        'post':Mypost,
        'cat':categories
    }
    return render(request,'home.html',data)

def post(request,url):
    mypost= Post.objects.get(url=url)
    return render(request,'post.html',{'post':mypost})


def cate(request,url):
    mycat = Category.objects.get(url=url)
    print(mycat.name)
    mypost = Post.objects.filter(cat=mycat)

    return render(request,'cate.html',{'post':mypost,'cate':mycat})