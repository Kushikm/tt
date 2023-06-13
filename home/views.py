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
  

#delete classroom
def delete_classroom(request, classroom_id):
    if request.method == 'POST':
        rooms = classroom.objects.get(id=classroom_id)
        rooms.delete()
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


def addsubjects(request):
    return render(request, 'addsubjects.html')

def room(request):
    allclass=classroom.objects.all()
    context={'addclass':allclass}
    return render(request,'room.html',context)    

def practical(request):
    return render(request,'practical.html')    


