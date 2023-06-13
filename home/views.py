from django.shortcuts import render, redirect
from home.models import classroom, instructor

# Create your views here.
def home(request):
    return render(request, 'home.html')

def addclassroom(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        ins = classroom(classnum=title)
        ins.save()
        context['success'] = True
    allLists = classroom.objects.all()
    context['addclassroom'] = allLists
    return render(request, 'addclassroom.html', context)
  


def theory(request):
    return render(request, 'theory.html')

def addinstructor(request):
    context = {'success': False}
    allLists = instructor.objects.all()
    
    if request.method == "POST":
        instructorid = request.POST.get('instructorid')
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        ins = instructor(instructorid=instructorid, name=name, designation=designation, email=email, phone=phone)
        ins.save()
        
        allLists = instructor.objects.all()
        context = {'success': True, 'addinstructor': allLists}

    return render(request, 'addinstructor.html', context)


def addsubjects(request):
    return render(request, 'addsubjects.html')

def room(request):
    allclass=classroom.objects.all()
    context={'addclass':allclass}
    return render(request,'room.html',context)    

def practical(request):
    return render(request,'practical.html')    


