from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signupStudent/$', views.signup_view_student, name='signupStudent'),
    url(r'^loginStudent/$', views.login_view_student, name='loginStudent'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^signupFaculty/$', views.signup_view_faculty, name='signupFaculty'),
    url(r'^loginFaculty/$', views.login_view_faculty, name='loginFaculty'),
]