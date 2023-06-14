from django.contrib import admin
from django.urls import path
from home import views
from . import views
from .views import delete_classroom
from .views import delete_instructor




urlpatterns = [
    

    path('home',views.home,name="home"),
    path('',views.home,name="home"),
    path('addclassroom',views.addclassroom,name="addclassroom"),
    path('addinstructor',views.addinstructor,name="addinstructor"),
    path('addsubjects',views.addsubjects,name="addsubjects"),
    path('deleteclassroom/<int:classroom_id>/', delete_classroom, name='delete-classroom'),
    #allotment paths
    path('deleteinstructor/<int:instructor_id>/', delete_instructor, name='delete_instructor'),

    path('theory',views.theory,name="theory"),
    path('room',views.room,name="room"),
     path('practical',views.practical,name="practical"),
     

]


