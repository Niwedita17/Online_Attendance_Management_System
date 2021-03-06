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


@admin.register(FacultyInfo)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('fid','f_fname', 'f_lname', 'email', 'phone', 'area_of_interest','btech','mtech','phd', 'house_no', 'street', 'city', 'state', 'pincode')
    ordering = ('fid',)
    search_fields = ('fid', 'f_fname')

@admin.register(CourseAttendance)
class CourseAttendanceAdmin(admin.ModelAdmin):
    list_display = ('sid','cid', 'date', 'attendance')
    ordering = ('sid',)
    search_fields = ('sid', 'cid')

@admin.register(CourseInfo)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('cid', 'cname', 'fid')
    ordering = ('cid',)
    search_fields = ('cid', 'cname')

admin.site.register(CourseRegistration)

