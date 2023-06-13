from django.shortcuts import render,redirect,HttpResponse
from home.models import classroom
from home.models import instructor
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



def addinstructor(request):
    context={'success':False}
    if request.method=="POST":
       instructorid = request.POST.get('instructorid')
       name = request.POST.get('name')
       designation = request.POST.get('designation')
       email = request.POST.get('email')
       phone = request.POST.get('phone')
       #print(name, email,phone,desc)
       ins =instructor(instructorid=instructorid,name=name,designation=designation, email=email, phone=phone )
       ins.save()
       context={'success':True}
      
    print("The data had been return to the db")
       
    #return HttpResponse("this is my contact page")
    return render(request, 'addinstructor.html')

def addsubjects(request):
    return render(request,'addsubjects.html')


#allotment section    

def theory(request):
    return render(request,'theory.html')    

def room(request):
    allclass=classroom.objects.all()
    context={'addclass':allclass}
    return render(request,'room.html',context)    

def practical(request):
    return render(request,'practical.html')    

