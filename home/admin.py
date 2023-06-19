from django.contrib import admin
from home.models import Classroom
from home.models import Subjects
from home.models import Theory,Room,Department,MeetingTime
from home.models import Instructor,Section
# Register your models here.


admin.site.register(Classroom)
admin.site.register(Instructor)
admin.site.register(Subjects)
admin.site.register(Theory)
admin.site.register(Room)

admin.site.register(Department)
admin.site.register(MeetingTime)
admin.site.register(Section)