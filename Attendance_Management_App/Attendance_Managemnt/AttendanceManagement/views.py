from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response


# Create your views here.
from django.template import RequestContext


def index(request):
    return render(request, 'AttendanceManagement/index.html')
