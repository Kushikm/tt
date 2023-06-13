from django.shortcuts import render,redirect,HttpResponse
from home.models import classroom
from .models import classroom



# Create your views here.
def home(request):
    #return HttpResponse("this is my home page")
    return render(request, 'home.html')

def addclassroom(request):
    context={'success':False}
    if request.method=="POST":
        title=request.POST['title']
        print(title)
        ins =classroom(classnum=title)
        ins.save()
        context={'success':True}
    allLists=classroom.objects.all()
    context={'addclassroom':allLists}    
    #return HttpResponse("this is my home page")
    return render(request, 'addclassroom.html',context)  

def theory(request):
    return render(request,'theory.html')

def addinstructor(request):
    return render(request,'addinstructor.html')

def addsubjects(request):
    return render(request,'addsubjects.html')

    

