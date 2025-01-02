"""
URL configuration for project3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='Home'),
    path('Aboutus/',Aboutus,name='Au'),
    path('Sports/',Sports,name='Sp'),
    path('Movies/',Movies,name='M'),
    path('cricket/',Cricket,name='CR'),
    path('Kabbadi/',Kabbadi,name='K'),
    path('Volleyball/',Volleyball,name='V'),
    path('Football/',Football,name='F'),
    path('Hockey/',Hockey,name='H'),
    path('Chess/',Chess,name='CH'),
    path('Anime/',Anime,name='A'),
    path('RajaSaab',RajaSaab,name='RS'),
    path('Salaar/',Salaar,name='S'),
    path('Chathrapathi/',Chathrapathi,name='C'),
    path('OG/',OG,name='O'),
    path('BeemlaNayak/',BeemlaNayak,name='BN'),
    path('Ustaad',Ustaad,name='U'),
    path('Demonslayer',Demonslayer,name='DS'),
    path('AOT/',AOT,name='AOT'),
    path('OnePiece/',OnePiece,name='OP'),
    path('HxH/',HxH,name='HxH'),
    path('BlackClover/',BlackClover,name='BLC'),
    path('TTIGRAAS/',TTIGRAAS,name='TTIGRAAS')
]
