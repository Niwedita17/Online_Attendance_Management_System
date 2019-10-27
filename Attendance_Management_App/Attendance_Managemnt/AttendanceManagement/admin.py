from django.contrib import admin

# Register your models here.
from .models import StudentInfo, FacultyInfo, CourseInfo, CourseRegistration, CourseAttendance

admin.site.register(StudentInfo)
admin.site.register(FacultyInfo)
admin.site.register(CourseInfo)
admin.site.register(CourseRegistration)
admin.site.register(CourseAttendance)

