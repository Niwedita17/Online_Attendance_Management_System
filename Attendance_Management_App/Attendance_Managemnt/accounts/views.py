from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from .models import StudentInfo
from .forms import StudentSignupForm


def index(request):
    return redirect('AttendanceManagement:index')


def signup_view(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            req_user = request.user
            form2.password = make_password(form.cleaned_data['password'])
            form2.save()
            user_instance = StudentInfo.objects.create(user=form2)
            user_instance.save()
                #user = form.save()
            # log the user in
            # username = form.cleaned_data.get('sid')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('AttendanceManagement:index')
    else:
        form = StudentSignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('AttendanceManagement:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/student-login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')
        #return render(request, 'accounts/logout.html')
        #return HttpResponseRedirect('/login/')