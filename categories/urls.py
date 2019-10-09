from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from .views import DisplayAllCategories

urlpatterns = [
    re_path(r'^categories/$', DisplayAllCategories.as_view(), name='Category view'),
   ]