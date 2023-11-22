from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
# Create your views here.
def homepage(request): #第一個一定是request
    posts=Post.objects.all()
    now=datetime.now()
    hour = now.timetuple().tm_hour
    return render(request,'index.html',locals())

def showpost(request,slug):
    post=Post.objects.get(slug=slug)
    if post !=None:
        return render(request,'post.html',locals())
    
def about(request):
    mhtml="<html><body><h1>I</h1><h3>am in NTUB</h3><body></html>"
    return HttpResponse(mhtml)

def about(request,num=-1):
    mhtml=f"<html><body><h1>I</h1><h3>am in NTUB</h3><h2>{num}</h2><body></html>" #要有f才會有數字
    return HttpResponse(mhtml)

import random
def about(request,num=-1):
    quotes = ['麥當勞',
                '炒飯',
                '炸醬麵',
                '泡麵',
                '火鍋',
                '熱狗蛋餅',
                '自助餐',
                '拉麵',
                '便當',
                '便利商店',
                '奶茶',
                '壽司',
                '燒臘',
                '健康餐']
    if num==-1 or num>14:
        
        quote = random.choice(quotes)
    else:
        quote=quotes[num]
    return render(request, 'about.html', locals())  

def carlist(request, maker=0):
	car_maker = ['Ford', 'Honda', 'Mazda']
	car_list = [[ {'model':'Fiesta', 'price': 203500},
                 {'model':'Focus','price': 605000},
                {'model':'Mustang','price': 900000}],
		        [{'model':'Fit', 'price': 450000}, 
		        {'model':'City', 'price': 150000}, 
		        {'model':'NSX', 'price':1200000}],
                [{'model':'Mazda3', 'price': 329999}, 
                {'model':'Mazda5', 'price': 603000},
                {'model':'Mazda6', 'price':850000}],]


	           
	maker = maker
	maker_name =  car_maker[maker]
	cars = car_list[maker]
	return render(request, 'carlist.html', locals())




'''
def homepage(request):
    posts=Post.objects.all() #把資料庫的東西傳上來
    post_lists=list()
    for counter,post in enumerate(posts): #enumerate回傳兩個值(index,data)
        post_lists.append(f'No.{counter}-{post} <br>') #br 換行
    return HttpResponse(post_lists)
'''