from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from .views import DisplayAllSubCategories

urlpatterns = [
    re_path(r'^subcategories/$', DisplayAllSubCategories.as_view(), name='SubCategory view'),
   ]