from django.contrib import admin
from home.models import Classroom
from home.models import Subjects
from home.models import Theory
from home.models import Instructor
# Register your models here.


admin.site.register(Classroom)
admin.site.register(Instructor)
admin.site.register(Subjects)
admin.site.register(Theory)