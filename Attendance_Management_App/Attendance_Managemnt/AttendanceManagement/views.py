from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response, get_object_or_404, get_list_or_404
from django.urls import reverse

from .models import StudentInfo, FacultyInfo,  CourseInfo, CourseRegistration, CourseAttendance
# Create your views here.
from django.template import RequestContext


def index(request):
    return render(request, 'AttendanceManagement/index.html')


def student_profile(request, sid):
    print("1")
    student_instance = get_object_or_404(StudentInfo, pk=sid)
    print("2")
    courses = get_list_or_404(CourseAttendance, sid=sid)
    final_list = []
    course_list = []
    for c in courses:
        if c.cid not in final_list:
            final_list.append(c.cid)
            course_list.append(c)
    for f in final_list:
         print(f)
    return render(request, 'AttendanceManagement/student-portal.html',
                  {"student_instance": student_instance, "courses_registered": course_list})


def student_registration(request, sid, cid):
    if request.method == 'post':
        reg = CourseRegistration(sid=sid, cid=cid)
        reg.save()
        return redirect('AttendanceManagement/student-registration.html')


"""def student_attendance(request, sid, cid):
    if request.method == 'POST':
        print("1")
        course_instance = get_object_or_404(CourseInfo, pk=cid)
        registered = get_list_or_404(CourseAttendance, sid=sid, cid=cid)
        faculty_instance = course_instance.fid

    #registered = get_list_or_404(CourseAttendance, pk=sid)
    #courses = registered.objects_all(registered.cid == cid)
        return render(request, 'AttendanceManagement/attendance.html', {"course_instance": course_instance,
                                                                    "faculty_instance": faculty_instance,
                                                                    "courses_registered": registered })


def reason_for_absence(request, sid, cid, date):
    if request.method == 'POST':
        t = CourseAttendance.objects.get( sid=sid, cid = cid,date= date)
        t.reason_for_absence = reason_for_absence  # change field
        t.save()  #
        return HttpResponseRedirect(reverse('AttendanceManagement:student_attendance', args=(sid,cid,)))
        #return render(request, 'AttendanceManagement/attendance.html')
"""

def faculty_profile(request, fid):
    faculty_instance = get_object_or_404(FacultyInfo, pk=fid)
    return render(request, 'AttendanceManagement/faculty-portal.html', {"faculty_instance" : faculty_instance})


def course_archive(request):
    courses = CourseInfo.objects.all()
    return render(request, 'AttendanceManagement/course-archive.html', {"all_courses": courses})


def course_detail(request, cid):
    if request.method == 'POST':
        print("0")
        course_instance = get_object_or_404(CourseInfo, pk=cid)
        faculty_instance = course_instance.fid
        return render(request, 'AttendanceManagement/course-single.html', {"course_instance": course_instance, "faculty_instance": faculty_instance})


# def student_registration(request, sid, cid):
#     if request.method == 'post':
#         reg = CourseRegistration(sid=sid, cid=cid)
#         reg.save()
#         return redirect('AttendanceManagement/student-registration')


