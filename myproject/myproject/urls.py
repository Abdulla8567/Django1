"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from basic.views import home, about, sample, sample1, product_info, filteringData, filter_city

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path("home/",home,name="home"),
    path("about/",about,name="about"),
    path("sample/",sample),
    path("sample1/",sample1),
    path("product_info/",product_info),
    path("filter/",filteringData),
    path("filter_city/",filter_city)
]
