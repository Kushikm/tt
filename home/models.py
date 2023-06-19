from django.db import models




# Create your models here.
time_slots = (
      ('8:00 - 9:00', '8:00 - 9:00'),
      ('9:00 - 10:00', '9:00 - 10:00'),
      ('10:30 - 11:30', '10:30 - 11:30'),
      ('11:30 - 12:30', '11:30 - 12:30'),
      ('2:00 - 3:00', '2:00 - 3:00'),
      ('3:00 - 4:00', '3:00 - 4:00'),
      ('4:00 - 5:00', '4:00 - 5:00'),
     )

DAYS_OF_WEEK = (
      ('Monday', 'Monday'),
      ('Tuesday', 'Tuesday'),
      ('Wednesday', 'Wednesday'),
      ('Thursday', 'Thursday'),
      ('Friday', 'Friday'),
      ('Saturday', 'Saturday'),
    )


class Instructor(models.Model):
    instructorid = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Subjects(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    sname = models.CharField(max_length=100)
    stype = models.CharField(max_length=20, default='2' , null=True)
    sem = models.CharField(max_length=20, default='3')
    credits = models.CharField(max_length=20, default='1')
    max_students = models.IntegerField(default=0)
    instructors = models.ManyToManyField(Instructor,max_length=100)
    def __str__(self):
        return self.sname

class Classroom(models.Model):
    classnum = models.CharField(max_length=30)
    seating_capacity = models.IntegerField(default=0)
    def __str__(self):
        return self.classnum

class Theory(models.Model):
    teacher_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=10, primary_key=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE,default='2')
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE,default='1')

    def __str__(self):
        return f"{self.subject_code} - {self.teacher_name}"
    
    def is_teacher_available(self, semester, day, slot):
        timetable_entries = self.timetable_set.filter(theory__instructor=self.instructor, semester=semester, day=day, slot=slot)
        return not timetable_entries.exists()

    def assign_teacher_to_slot(self, semester, day, slot):
        timetable_entry = self.timetable_set.create(theory=self, semester=semester, day=day, slot=slot)
    
class Room(models.Model):
    semester_number = models.CharField(max_length=20,unique=True)
    room_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"Semester {self.semester_number} - Room {self.room_name}"


'''class Timetable(models.Model):
    theory = models.ForeignKey(Theory, on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)
    day = models.PositiveSmallIntegerField()
    slot = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.theory} - Semester: {self.semester}, Day: {self.day}, Slot: {self.slot}"'''
    


class Department(models.Model):

    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('MECH', 'Mechanical Engineering'),
        ('CIVIL', 'Civil Engineering'),
        # Add more choices for other engineering branches
    ]
    depname = models.CharField(max_length=30,choices=DEPARTMENT_CHOICES)
    courses = models.ManyToManyField(Subjects,max_length=100)
    def __str__(self):
        return self.depname   
    


class MeetingTime(models.Model):
    pid = models.CharField(max_length=4, primary_key=True)
    time = models.CharField(max_length=50, choices=time_slots, default='11:30 - 12:30')
    day = models.CharField(max_length=15, choices=DAYS_OF_WEEK)

    def __str__(self):
        return f'{self.pid} {self.day} {self.time}'
    


class Section(models.Model):
    section_id = models.CharField(max_length=25, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    num_class_in_week = models.IntegerField(default=0)
    course = models.ForeignKey(Subjects, on_delete=models.CASCADE, blank=True, null=True)
    theory = models.ForeignKey(Theory, on_delete=models.CASCADE, blank=True, null=True)
    meeting_time = models.ForeignKey(MeetingTime, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=True, null=True)

    def set_room(self, room):
        section = Section.objects.get(pk = self.section_id)
        section.room = room
        section.save()

    def set_meetingTime(self, meetingTime):
        section = Section.objects.get(pk = self.section_id)
        section.meeting_time = meetingTime
        section.save()

    def set_instructor(self, instructor):
        section = Section.objects.get(pk=self.section_id)
        section.instructor = instructor
        section.save()
