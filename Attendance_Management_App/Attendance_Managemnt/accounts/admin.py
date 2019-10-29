from django.contrib import admin

from .forms import StudentSignupForm
from .models import StudentInfo, FacultyInfo, CourseInfo, CourseRegistration, CourseAttendance
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


@admin.register(StudentInfo)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('sid', 's_fname', 's_lname', 'email', 'phone', 'degree', 'house_no', 'street', 'city', 'state', 'pincode')
    ordering = ('sid',)
    search_fields = ('sid', 's_fname')


admin.site.register(FacultyInfo)
admin.site.register(CourseInfo)
admin.site.register(CourseRegistration)
admin.site.register(CourseAttendance)
