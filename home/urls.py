from django.contrib import admin
from django.urls import path
from home import views
from . import views




urlpatterns = [
    

    path('home',views.home,name="home"),
    path('',views.home,name="home"),
    path('addclassroom',views.addclassroom,name="addclassroom"),
    path('addinstructor',views.addinstructor,name="addinstructor"),
    path('addsubjects',views.addsubjects,name="addsubjects"),
    #allotment paths
    path('theory',views.theory,name="theory"),
    path('room',views.room,name="room"),
     path('practical',views.practical,name="practical"),
]

