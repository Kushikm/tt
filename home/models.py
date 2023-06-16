from django.db import models




# Create your models here.
class Instructor(models.Model):
    instructorid = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=20, default='professor')
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Subjects(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    stype = models.CharField(max_length=20, default='2' , null=True)
    sem = models.CharField(max_length=20, default='3')
    credits = models.CharField(max_length=20, default='1')

    def __str__(self):
        return self.name

class Classroom(models.Model):
    classnum = models.CharField(max_length=30)

    def __str__(self):
        return self.classnum

class Theory(models.Model):
    teacher_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=10, primary_key=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE,default='2')
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE,default='1')

    def __str__(self):
        return f"{self.subject_code} - {self.teacher_name}"
    

           