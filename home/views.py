from django.shortcuts import render, redirect
from home.models import Classroom, Instructor, Subjects

def home(request):
    return render(request, 'home.html')

def addclassroom(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        ins = Classroom(classnum=title)
        ins.save()
        context['success'] = True
    allLists = Classroom.objects.all()
    context['addclassroom'] = allLists
    return render(request, 'addclassroom.html', context)

def delete_classroom(request, classroom_id):
    if request.method == 'POST':
        room = Classroom.objects.get(id=classroom_id)
        room.delete()
        return redirect('addclassroom')
    else:
        # Handle GET request if necessary
        pass

def delete_subjects(request, subjects_id):
    if request.method == 'POST':
        room = Subjects.objects.get(codeid=subjects_id)
        room.delete()
        return redirect('addsubjects')
    else:
        # Handle GET request if necessary
        pass   

def delete_instructor(request, instructor_id):
    if request.method == 'POST':
        ins =  Instructor.objects.get(instructorid=instructor_id)
        ins.delete()
        return redirect('addinstructor')
    else:
        # Handle GET request if necessary
        pass


def theory(request):
    allteach = Instructor.objects.all()
    theory_courses = Subjects.objects.filter(type='theory')
    context = {
        'addteacher': allteach,
        'theory_courses': theory_courses
    }
    return render(request, 'theory.html', context)

def addinstructor(request):
    context = {'success': False}

    if request.method == "POST":
        instructorid = request.POST.get('instructorid')
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        ins = Instructor(
            instructorid=instructorid,
            name=name,
            designation=designation,
            email=email,
            phone=phone
        )
        ins.save()
        context['success'] = True

    allinst = Instructor.objects.all()
    context['addinstructor'] = allinst
    return render(request, 'addinstructor.html', context)

def addsubjects(request):
    context = {'success': False}

    if request.method == "POST":
        code = request.POST.get('code')
        name = request.POST.get('name')
        type = request.POST.get('type')
        sem = request.POST.get('sem')
        credits = request.POST.get('credits')

        ins = Subjects(code=code, name=name, type=type, sem=sem, credits=credits)
        ins.save()
        context['success'] = True

    allinst = Subjects.objects.all()
    context['addsubjects'] = allinst
    return render(request, 'addsubjects.html', context)

def room(request):
    allclass = Classroom.objects.all()
    context = {'addclass': allclass}
    return render(request, 'room.html', context)

def practical(request):
    return render(request, 'practical.html')