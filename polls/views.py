from django.shortcuts import render
from django.http import HttpResponse
from polls.models import image,Contact,Post
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum, Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
def index(request):
    return render(request,'polls\index.html')
def artweek(request):
    return render(request,'polls\page1.html')
def artyear(request):
    return render(request,'polls\page2.html')
def arthall(request):
    return render(request,'polls\page3.html')
def artexhibit(request):
    template_name ='polls\page4.html'
    img=image.objects.all()
    return render(request,'polls\page4.html',{'image':img})
def artsign(request):
    return render(request,'polls\page5.html')
def artsubmit(request):
    return render(request,'polls\page6.html')
#def highart:
