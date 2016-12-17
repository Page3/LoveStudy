"""LoveStudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from TestPlatform import views as learn_views  # new
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='static/icons/favicon.ico', permanent=True)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',learn_views.index),
    url(r'^api/getPictures$',learn_views.getPictures),
    url(r'^api/getLists$',learn_views.getLists),
    url(r'^api/getUserDetail$',learn_views.getUserDetail),
    url(r'^api/getFavourites$',learn_views.getFavourites),
    url(r'^api/getUploads$',learn_views.getUploads),
    url(r'^api/getArticles$',learn_views.getArticles),
    url(r'^api/setCollege$',learn_views.setCollege),
    url(r'^api/addFavourite$',learn_views.addFavourite),
    url(r'^api/rmFavourite$',learn_views.rmFavourite),
    url(r'^favicon\.ico$', favicon_view),
]
