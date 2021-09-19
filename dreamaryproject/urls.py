"""dreamaryproject URL Configuration

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
# from, import 늘 꼭 확인하기
from django.contrib import admin
from django.urls import path, include
from page import views
from django.conf import settings
from django.conf.urls.static import static
#첨에 디폴트 주소로 들어왔을때, 페이지.유알엘 인클루드하니까 앱 내 유알엘에서 패스 설정
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#url만들기: path('new/',views.new, name='new),
#collectstatic은 배포전에 해도 ㅇㅋ
# 프로젝트에서는 각각의 앱으로 넘어가는 패스만 설정해준다.