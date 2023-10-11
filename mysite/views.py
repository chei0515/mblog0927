from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def homepage(request):
    posts=Post.objects.all()
    now=datetime.now()
    return render(request,'index.html',locals())

def showpost(request,slug):
    post=Post.objects.get(slug=slug)
    return render(request,'post.html',locals())
'''
def homepage(request):
    posts=Post.objects.all() #把資料庫的東西傳上來
    post_lists=list()
    for counter,post in enumerate(posts): #enumerate回傳兩個值(index,data)
        post_lists.append(f'No.{counter}-{post} <br>') #br 換行
    return HttpResponse(post_lists)
'''