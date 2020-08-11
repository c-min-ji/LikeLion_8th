"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
#blog.views 를 추가로 import 해준다.
#import blog.views
from django.conf.urls import url, handler404

import handlerpage.views

handler404 = 'handlerpage.views.handler404'

#index path를 추가한다.
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', blog.views.index, name="index"),
    url('',include('blog.urls'))
]
