from django.contrib import admin
from .models import dept, student,Course,Attendance

# Register your models here.
admin.site.register(student)
admin.site.register(Course)
admin.site.register(Attendance)
admin.site.register(dept)

