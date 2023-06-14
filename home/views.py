from django.shortcuts import render, redirect
from home.models import classroom, instructor, subjects

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
  

#delete classroom
def delete_classroom(request, classroom_id):
    if request.method == 'POST':
        rooms = classroom.objects.get(id=classroom_id)
        rooms.delete()
        return redirect('addclassroom')  # Redirect to the desired page after deletion
    else:
        # Handle GET request if necessary
       pass   
def delete_instructor(request, instructor_id):
    if request.method == 'POST':
        ins1  = instructor.objects.get(id=instructor_id)
        ins1.delete()
        return redirect('addclassroom')  # Redirect to the desired page after deletion
    else:
        # Handle GET request if necessary
       pass       


def theory(request):
    return render(request, 'theory.html')

def addinstructor(request):
    context = {'success': False}
    
    if request.method == "POST":
        instructorid = request.POST.get('instructorid')
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        ins = instructor(instructorid=instructorid, name=name, designation=designation, email=email, phone=phone)
        ins.save()
        context['success'] = True
        
    allinst = instructor.objects.all()
    context['addinstructor'] = allinst
    return render(request, 'addinstructor.html', context)




def room(request):
    allclass=classroom.objects.all()
    context={'addclass':allclass}
    return render(request,'room.html',context)    

def practical(request):
    return render(request,'practical.html')    

def addsubjects(request):
    context = {'success': False}
    
    if request.method == "POST":
        code = request.POST.get('code')
        name = request.POST.get('name')
        type = request.POST.get('type')
        sem = request.POST.get('sem')
        
        
        ins = subjects(code=code, name=name, type=type, sem=sem)
        ins.save()
        context['success'] = True
        
    allinst = subjects.objects.all()
    context['addsubjects'] = allinst
    return render(request, 'addsubjects.html', context)


    