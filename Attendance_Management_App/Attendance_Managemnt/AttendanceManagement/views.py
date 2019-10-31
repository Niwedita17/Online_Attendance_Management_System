from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.utils.datetime_safe import date

from .models import StudentInfo, FacultyInfo,  CourseInfo, CourseRegistration, CourseAttendance
# Create your views here.
from django.template import RequestContext


def index(request):
    return render(request, 'AttendanceManagement/index.html')


def studentprofile(request,sid):
    student_instance = StudentInfo.objects.get(sid=sid)
    return render(request, 'AttendanceManagement/student-portal.html',
                  {"student_instance": student_instance})


def student_profile(request, sid):
    print("1")
    student_instance = get_object_or_404(StudentInfo, pk=sid)
    print("2")
    #courses = get_list_or_404(CourseAttendance, sid=sid)

    try:
        courses = get_list_or_404(CourseAttendance, sid=sid)

        print(len(courses))
        final_list = []
        course_list = []
        for c in courses:
            if c.cid not in final_list:
                final_list.append(c.cid)
                course_list.append(c)
        for f in final_list:
             print(f)
        return render(request, 'AttendanceManagement/student-portal.html',
                      {"student_instance": student_instance, "courses":final_list})
    except:
        return render(request, 'AttendanceManagement/student-portal.html',
                      {"student_instance": student_instance, "courses.cid":'No courses registered'})


def view_attendance(request):
    if request.method == "POST":  # view existing booking
        cid = request.POST['cid']
        print(cid)
        if cid:
            course = get_list_or_404(CourseAttendance, cid=cid)
            return render(request, 'AttendanceManagement/attendance.html', {'course': course,'cid':cid})
        else:
            return render(request, 'AttendanceManagement/student-portal.html', {'error_message_booking': 'No booking found'})


def give_attendance(request):
    if request.method == "POST":
        # course = CourseAttendance.objects.get(cid=cid)
        course1 = request.POST['cid']
        course_object = get_object_or_404(CourseInfo,cid=course1)
        course = get_list_or_404(CourseAttendance, cid=course1)
        student = request.POST['sid']
        student_object = get_object_or_404(StudentInfo, sid=student)
        my_sid = student_object.sid
        my_cid= course_object.cid
        date1 = date.today()
        attendance = request.POST['attendance']
        reason = 'nill'
        attendance_instance = CourseAttendance(cid=course_object, sid=student_object, date=date1, attendance=attendance)
        attendance_instance.save()
        f1=request.POST['fid']
        faculty_object = get_object_or_404(FacultyInfo,pk=f1)

        return HttpResponseRedirect(reverse('AttendanceManagement:faculty', args=(f1,)))
    else:
        return render(request, 'AttendanceManagement/faculty-portal.html')


def facultyprofile(request,fid):
    faculty_instance = FacultyInfo.objects.get(fid=fid)
    return render(request, 'AttendanceManagement/faculty-portal.html',
                  {"faculty_instance": faculty_instance,"give_attendance":False})


def faculty_profile(request, fid):
    faculty_instance = get_object_or_404(FacultyInfo, pk=fid)
    print(faculty_instance.f_fname)
    try:
        courses_list = get_list_or_404(CourseInfo,fid=fid)
        final_list = []
        course_list = []
        for c in courses_list:
            if c.cid not in final_list:
                final_list.append(c.cid)
                course_list.append(c)
        for f in final_list:
            print(f)
        return render(request, 'AttendanceManagement/faculty-portal.html',
                      {"faculty_instance": faculty_instance, "courses": course_list, "give_attendance":True})
        #return render(request, 'AttendanceManagement/faculty-portal.html', {"faculty_instance" : faculty_instance})
    except:
        return render(request, 'AttendanceManagement/faculty-portal.html', {"faculty_instance": faculty_instance, "courses.cid": 'no course taken', "give_attendance":False})


def course_archive(request):
    courses = CourseInfo.objects.all()
    return render(request, 'AttendanceManagement/course-archive.html', {"all_courses": courses})


def course_detail(request, cid):
    if request.method == 'POST':
        print("0")
        course_instance = get_object_or_404(CourseInfo, pk=cid)
        faculty_instance = course_instance.fid
        return render(request, 'AttendanceManagement/course-single.html', {"course_instance": course_instance, "faculty_instance": faculty_instance})

