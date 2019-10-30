from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from .models import StudentInfo, FacultyInfo, User
# Create your views here.
from django.template import RequestContext


def index(request):
    return render(request, 'AttendanceManagement/index.html')


def student_profile(request, sid):
    student_instance = get_object_or_404(StudentInfo, pk=sid)
    return render(request, 'AttendanceManagement/student-portal.html', {"student_instance" : student_instance})


def faculty_profile(request, fid):
    faculty_instance = get_object_or_404(FacultyInfo, pk=fid)
    return render(request, 'AttendanceManagement/faculty-portal.html', {"faculty_instance" : faculty_instance})