from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from .models import StudentInfo
from .forms import StudentSignupForm, FacultySignupForm


def index(request):
    return redirect('AttendanceManagement:index')


def signup_view_student(request):
    # if this is a POST request we need to process the form data
    template = 'accounts/signup.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentSignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['sid']).exists():
                print("1")
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                print("2")
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password2']:
                print("3")
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                print("4")
                # save the table info to the database
                form.save()
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['sid'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.s_fname = form.cleaned_data['s_fname']
                user.s_lname = form.cleaned_data['s_lname']
                user.phone = form.cleaned_data['phone']
                user.degree = form.cleaned_data['degree']
                user.house_no = form.cleaned_data['house_no']
                user.street = form.cleaned_data['street']
                user.city = form.cleaned_data['city']
                user.state = form.cleaned_data['state']
                user.pincode = form.cleaned_data['pincode']
                user.save()

                user_id = user.username
                # Login the user
                login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect(reverse('AttendanceManagement:student', args=(user_id,)))

    # No post data available, let's just show the page.
    else:
        print("6")
        form = StudentSignupForm()
    return render(request, template, {'form': form})


def login_view_student(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            # get user id
            user_id = user.username
            login(request, user)
            return HttpResponseRedirect(reverse('AttendanceManagement:student', args=(user_id,)))
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/student-login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('AttendanceManagement:index')


def signup_view_faculty(request):
    # if this is a POST request we need to process the form data
    template = 'accounts/signup.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FacultySignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['fid']).exists():
                print("1")
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                print("2")
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password2']:
                print("3")
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                print("4")
                # save the table info to the database
                form.save()
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['fid'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.f_fname = form.cleaned_data['f_fname']
                user.f_lname = form.cleaned_data['f_lname']
                user.phone = form.cleaned_data['phone']
                user.area_of_interest = form.cleaned_data['area_of_interest']
                user.btech = form.cleaned_data['btech']
                user.mtech = form.cleaned_data['mtech']
                user.phd = form.cleaned_data['phd']
                user.house_no = form.cleaned_data['house_no']
                user.street = form.cleaned_data['street']
                user.city = form.cleaned_data['city']
                user.state = form.cleaned_data['state']
                user.pincode = form.cleaned_data['pincode']
                user.save()

                user_id = user.username
                # Login the user
                login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect(reverse('AttendanceManagement:faculty', args=(user_id,)))
    # No post data available, let's just show the page.
    else:
        print("6")
        form = StudentSignupForm()
    return render(request, template, {'form': form})


def login_view_faculty(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            # get user id
            user_id = user.username
            login(request, user)
            return HttpResponseRedirect(reverse('AttendanceManagement:faculty', args=(user_id,)))
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/faculty-login.html', {'form': form})



