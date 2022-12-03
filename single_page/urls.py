from django.contrib import admin
from django.urls import path
from single_page.views import *

app_name='single_page'
urlpatterns = [
    path("",index_view , name='index'),


]
