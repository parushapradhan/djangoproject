"""artistry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('',views.index,name='index'),
    path('index.html',views.index,name='index.html'),
    path('page1.html',views.artweek,name='page1.html'),
    path('page2.html',views.artyear,name='page2.html'),
    path('page3.html',views.arthall,name='page3.html'),
    path('page4.html',views.artexhibit,name='page4.html'),
    path('page5.html',views.artsign,name='page5.html'),
    path('page6.html',views.artsubmit,name='page6.html'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout,name='logout'),
]
