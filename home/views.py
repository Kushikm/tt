from django.shortcuts import render, redirect
from home.models import Classroom, Instructor, Subjects,Theory,Room,Department,MeetingTime,Section
import psycopg2
from home.models import time_slots, DAYS_OF_WEEK
import random



POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.05


class Data:
    def __init__(self):
        self._rooms = Classroom.objects.all()
        self._meetingTimes = MeetingTime.objects.all()
        self._instructors = Instructor.objects.all()
        self._courses = Subjects.objects.all()
        self._depts = Department.objects.all()

    def get_rooms(self): return self._rooms

    def get_instructors(self): return self._instructors

    def get_courses(self): return self._courses

    def get_depts(self): return self._depts

    def get_meetingTimes(self): return self._meetingTimes


class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numberOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True

    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes

    def get_numbOfConflicts(self): return self._numberOfConflicts

    def get_fitness(self):
        if self._isFitnessChanged:
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    def initialize(self):
        sections = Section.objects.all()
        
        for section in sections:
            dept = section.department
            n = section.num_class_in_week
            if n <= len(MeetingTime.objects.all()):
                courses = dept.courses.all()
                for course in courses:
                    stype = course.stype
                   
                    for i in range(n // len(courses)):
                        crs_inst = course.instructors.all()
                        newClass = Class(self._classNumb, dept, section.section_id, course,stype)
                        self._classNumb += 1
                        meeting_times = data.get_meetingTimes()
                        meeting_rooms=data.get_rooms()
                        if stype == "Practical":  # Allocate 3-hour time slot for practical subjects
                            meeting_times = data.get_meetingTimes().filter(duration=3)
                            meeting_rooms=data.get_rooms().filter(rtype='Lab')
                        newClass.set_meetingTime(meeting_times[random.randrange(len(meeting_times))])
                        newClass.set_room(meeting_rooms[random.randrange(len(meeting_rooms))])
                        newClass.set_instructor(crs_inst[random.randrange(len(crs_inst))])
                        self._classes.append(newClass)
            else:
                n = len(MeetingTime.objects.all())
                courses = dept.courses.all()
                for course in courses:
                    stype = course.stype
                    for i in range(n // len(courses)):
                        crs_inst = course.instructors.all()
                        newClass = Class(self._classNumb, dept, section.section_id, course,stype)
                        self._classNumb += 1
                        meeting_times = data.get_meetingTimes()
                        meeting_rooms=data.get_rooms()
                        if stype == "Practical":  # Allocate 3-hour time slot for practical subjects
                            meeting_times = data.get_meetingTimes().filter(duration=3)
                            meeting_rooms=data.get_rooms().filter(rtype='Lab')
                        newClass.set_meetingTime(meeting_times[random.randrange(len(meeting_times))])
                        newClass.set_room(meeting_rooms[random.randrange(len(meeting_rooms))])
                        newClass.set_instructor(crs_inst[random.randrange(len(crs_inst))])
                        self._classes.append(newClass)

        return self


    def calculate_fitness(self):
        self._numberOfConflicts = 0
        classes = self.get_classes()
        for i in range(len(classes)):
            if classes[i].room.seating_capacity < int(classes[i].course.max_students):
                self._numberOfConflicts += 1
            for j in range(len(classes)):
                if j >= i:
                    if (classes[i].meeting_time == classes[j].meeting_time) and \
                            (classes[i].section_id != classes[j].section_id) and (classes[i].section == classes[j].section):
                        if classes[i].room == classes[j].room:
                            self._numberOfConflicts += 1
                        if classes[i].instructor == classes[j].instructor:
                            self._numberOfConflicts += 1
        return 1 / (1.0 * self._numberOfConflicts + 1)


class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = [Schedule().initialize() for i in range(size)]

    def get_schedules(self):
        return self._schedules


class GeneticAlgorithm:
    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))

    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if random.random() > 0.5:
                crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule

    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(len(mutateSchedule.get_classes())):
            if MUTATION_RATE > random.random():
                mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule

    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop.get_schedules()[random.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop
    


class Class:
    def __init__(self, id, dept, section, course,stype):
        self.section_id = id
        self.department = dept
        self.course = course
        self.instructor = None
        self.meeting_time = None
        self.room = None
        self.section = section
        self.stype = stype
        

    def get_id(self): return self.section_id

    def get_dept(self): return self.department

    def get_course(self): return self.course

    def get_instructor(self): return self.instructor

    def get_meetingTime(self): return self.meeting_time

    def get_room(self): return self.room

    def get_room(self): return self.stype
  

    def set_instructor(self, instructor): self.instructor = instructor

    def set_meetingTime(self, meetingTime): self.meeting_time = meetingTime

    def set_room(self, room): self.room = room



data = Data()


def context_manager(schedule):
    classes = schedule.get_classes()
    context = []
    cls = {}
    for i in range(len(classes)):
        cls["section"] = classes[i].section_id
        cls['dept'] = classes[i].department.dept_name
        cls['course'] = f'{classes[i].course.course_name} ({classes[i].course.course_number}, ' \
                        f'{classes[i].course.max_numb_students}'
        cls['room'] = f'{classes[i].room.r_number} ({classes[i].room.seating_capacity})'
        cls['instructor'] = f'{classes[i].instructor.name} ({classes[i].instructor.uid})'
        cls['meeting_time'] = [classes[i].meeting_time.pid, classes[i].meeting_time.day, classes[i].meeting_time.time]
        context.append(cls)
    return context










'''viewss'''
def home(request):
    return render(request, 'home.html')

def mastertime(request):
    # Retrieve the necessary data for the master timetable (time_slots, weekdays, schedule)
    time_slots = ['8:00 - 9:00', '9:00 - 10:00', '10:30 - 11:30', '11:30 - 12:30', '2:00 - 3:00', '3:00 - 4:00', '4:00 - 5:00','2:00 - 5:00','10:15 - 1:15']
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday']
    # Retrieve the schedule data based on your application logic
    schedule = []
    population = Population(POPULATION_SIZE)
    generation_num = 0
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    geneticAlgorithm = GeneticAlgorithm()
    while population.get_schedules()[0].get_fitness() != 1.0:
        generation_num += 1
        print('\n> Generation #' + str(generation_num))
        population = geneticAlgorithm.evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        schedule = population.get_schedules()[0].get_classes()
    

    return render(request, 'mastertime.html', {'schedule': schedule, 'sections': Section.objects.all(),
                                              'times': MeetingTime.objects.all(),'weekdays': weekdays,'time_slots':time_slots})


def timetable(request):
    schedule = []
    population = Population(POPULATION_SIZE)
    generation_num = 0
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    geneticAlgorithm = GeneticAlgorithm()
    while population.get_schedules()[0].get_fitness() != 1.0:
        generation_num += 1
        print('\n> Generation #' + str(generation_num))
        population = geneticAlgorithm.evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        schedule = population.get_schedules()[0].get_classes()
     # Retrieve all meeting times from the database
      # Create an instance of the Data class
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    time_slots =  ['8:00 - 9:00', '9:00 - 10:00', '10:30 - 11:30', '11:30 - 12:30', '2:00 - 3:00', '3:00 - 4:00', '4:00 - 5:00','2:00 - 5:00','10:15 - 1:15']
    
    return render(request, 'gentimetable.html', {'schedule': schedule, 'sections': Section.objects.all(),
                                              'times': MeetingTime.objects.all(),'weekdays': weekdays,'time_slots':time_slots})

   







def addclassroom(request):
    context = {'success': False}
    if request.method == "POST":
        classnum = request.POST.get('classnum')
        seating_capacity =request.POST.get('seating_capacity')
        rtype=request.POST.get('rtype')
        if seating_capacity:
         ins = Classroom(classnum=classnum,seating_capacity =seating_capacity,rtype=rtype)
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
        sname = request.POST.get('sname')
        stype = request.POST.get('stype')
        sem = request.POST.get('sem')
        credits = request.POST.get('credits')
        max_students=request.POST.get('max_students')
        instructors=request.POST.getlist('instructors[]')
       
        if sname: 
         
         ins = Subjects(code=code, sname=sname, stype=stype, sem=sem, credits=credits,max_students=max_students)
         if stype == "Practical":
            lab_name = request.POST.get('labName')  # Retrieve lab name from the form
            ins.lab_name = lab_name
         ins.save()
         for instructor_name in instructors:
            instructor, _ = Instructor.objects.get_or_create(name=instructor_name)
            ins.instructors.add(instructor)

         context['success'] = True
    allins=Instructor.objects.all()
    allsubjects = Subjects.objects.all()
    context = {'addsubjects':allsubjects,
               'allins':allins}
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
        ins = Instructor(
            instructorid=instructorid,
            name=name,
           
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
        instructor = Instructor.objects.get(name=teacher_name)
        subject = Subjects.objects.get(code=subject_code)
       
        theory_allotment = Theory(
            subject_code=subject_code,
            teacher_name=teacher_name,
            instructor=instructor,
            subject=subject,
        )
        theory_allotment.save()
        context['success'] = True

        
    
    allteach = Instructor.objects.all()
    theory_courses = Subjects.objects.filter(stype='Theory')
    theory_allotments = Theory.objects.all().select_related('instructor', 'subject')
    
    context ={
        'addteacher': allteach,
        'theorycourses': theory_courses,
        'theory_allotments': theory_allotments,
    }
    return render(request, 'theory.html', context)

def adddepartment(request):
     context = {'success': False}

     if request.method == "POST":
       depname = request.POST.get('depname')
       courses= request.POST.getlist('courses[]')
       if depname:
        departallot = Department(
            depname=depname,
            
        )
        departallot.courses.set(courses)
        departallot.save()
        context['success'] = True
     engineering_branches = Department.DEPARTMENT_CHOICES
     departallot=Department.objects.all()   
     allcourses=Subjects.objects.all()
     context={
         'allcourses':allcourses,
         'departallot': departallot,
         'engineering_branches':engineering_branches,
     }
     return render(request,'adddepartment.html',context)


def room(request):
    context = {'success': False}

    if request.method == "POST":
        semester_number = request.POST.get('semester_number')
        room_name  = request.POST.get('room_name')
        room_allot = Room(
            semester_number=semester_number,
            room_name =room_name ,

        )
        room_allot.save()
        context['success'] = True

    room_allot=Room.objects.all()
    allsem = Subjects.objects.values_list('sem', flat=True).distinct()
    allclsnum = Classroom.objects.values_list('classnum', flat=True).distinct()
    context={
        'room_allot':room_allot,
        'allsem':allsem,
        'allclsnum':allclsnum,
    }    
    
    return render(request, 'room.html', context)



def addtimings(request):
    context = {'success': False}

    if request.method == "POST":
        pid=request.POST.get('pid')
        time=request.POST.get('time')
        day=request.POST.get('day')
        duration=request.POST.get('duration')
        all_times=MeetingTime(
            pid=pid,
            time=time,
            day=day,
            duration=duration,
        )
        all_times.save()
    all_times=MeetingTime.objects.all()    
    timess = time_slots
    dayss = DAYS_OF_WEEK    
    context = {
        'all_times': all_times,
        'timess': timess,
        'dayss': dayss,
         }

    return render(request,'addtimings.html',context)

def delete_timimg(request, p_id):
    if request.method == 'POST':
        ins =  MeetingTime.objects.get(pid=p_id)
        ins.delete()
        return redirect('addtimings')
    else:
        # Handle GET request if necessary
        pass

def practical(request):
    return render(request, 'practical.html')



def addsection(request):
    context = {'success': False}

    if request.method == "POST":
        section_id=request.POST.get('section_id')
        department_name=request.POST.get('department')
        num_class_in_week=request.POST.get('num_class_in_week')
        department_id = int(department_name)
        department = Department.objects.get(id=department_id)
        allsec=Section(
            section_id=section_id,
            department=department,
            num_class_in_week=num_class_in_week,
        )
        allsec.save()
    engineering_branches = Department.objects.all()   
    allsec=Section.objects.all() 
    context={
        'allsec':allsec,
        'engineering_branches':engineering_branches,
    }   
    return render(request,'addsection.html',context)

def delete_section(request, p_id):
    if request.method == 'POST':
        ins =  Section.objects.get(section_id=p_id)
        ins.delete()
        return redirect('addsection')
    else:
        # Handle GET request if necessary
        pass