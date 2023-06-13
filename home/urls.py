from django.contrib import admin
from django.urls import path
from home import views
from . import views




urlpatterns = [
    
    path('home',views.home,name="home"),
    path('',views.home,name="home"),
    path('addclassroom',views.addclassroom,name="addclassroom"),
    path('theory',views.theory,name="theory"),
]
