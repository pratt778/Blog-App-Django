from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('home/<url>',views.post,name='post'),
    path('category/<url>',views.cate,name='cats'),
]
