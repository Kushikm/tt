from django.shortcuts import render, redirect
from home.models import Classroom, Instructor, Subjects,Theory

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


def addsubjects(request):
    context = {'success': False}

    if request.method == "POST":
        code = request.POST.get('code')
        name = request.POST.get('name')
        stype = request.POST.get('stype')
        sem = request.POST.get('sem')
        credits = request.POST.get('credits')

        ins = Subjects(code=code, name=name, stype=stype, sem=sem, credits=credits)
        ins.save()
        context['success'] = True

    allsubjects = Subjects.objects.all()
    context['addsubjects'] = allsubjects
    return render(request, 'addsubjects.html', context)


def delete_subjects(request, subjects_code):
    if request.method == 'POST':
      ins = Subjects.objects.get(code=subjects_code)
      ins.delete()
      return redirect('addsubjects')
    else:
         pass

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

def delete_instructor(request, instructor_id):
    if request.method == 'POST':
        ins =  Instructor.objects.get(instructorid=instructor_id)
        ins.delete()
        return redirect('addinstructor')
    else:
        # Handle GET request if necessary
        pass


def theory(request):
    context = {'success': False}

    if request.method == "POST":
        subject_code = request.POST.get('subject_code')
        teacher_name = request.POST.get('teacher_name')
         
        subject = Subject.objects.get(code=subject_code)
        teacher = Teacher.objects.get(name=teacher_name)

        ins = Theory(
                subject_code=subject_code,
                teacher_name=teacher_name,
                teacher_id=teacher.id,
                teacher_designation=teacher.designation,
                subject_name=subject.name,
                # Set other fields as needed
            )
        ins.save()
        context['success'] = True
 


    allteach = Instructor.objects.all()
    theory_courses = Subjects.objects.filter(stype='Theory')
    context = {
        'addteacher': allteach,
        'theorycourses': theory_courses,
    }
    return render(request, 'theory.html', context)



def room(request):
    allclass = Classroom.objects.all()
    context = {'addclass': allclass}
    return render(request, 'room.html', context)

def practical(request):
    return render(request, 'practical.html')