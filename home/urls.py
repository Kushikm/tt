from django.contrib import admin
from django.urls import path
from home import views
from . import views
from .views import delete_classroom
from .views import delete_instructor
from .views import delete_subjects




urlpatterns = [
    

    path('home',views.home,name="home"),
    path('',views.home,name="home"),
    path('timetable_generation/', views.timetable, name='timetable'),
    path('addclassroom',views.addclassroom,name="addclassroom"),
    path('addtimings', views.addtimings, name='addtimings'),
    path('adddepartment', views.adddepartment, name='adddepartment'),
    path('addinstructor/',views.addinstructor,name="addinstructor"),
    path('addsubjects',views.addsubjects,name="addsubjects"),
     path('addsection',views.addsection,name="addsection"),
    path('deleteclassroom/<int:classroom_id>/', delete_classroom, name='delete-classroom'),
    path('deletesubjects/<str:subjects_code>/', delete_subjects, name='delete-subjects'),
    #allotment paths
    path('deleteinstructor/<str:instructor_id>/', delete_instructor, name='delete-instructor'),
     path('mastertime/', views.mastertime, name='mastertime'),


    path('theory',views.theory,name="theory"),
    path('room',views.room,name="room"),
     path('practical',views.practical,name="practical"),
     

]


