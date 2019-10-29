from django.conf.urls import url
from . import views as user_views
from django.contrib.auth import views as auth_views

app_name = 'AttendanceManagement'

urlpatterns = [
    url(r'^$', user_views.index, name='index'),
    #127.0.0.1/attendance/
    url(r'^student/(?P<sid>[0-9]{2}[A-Z]{2}[0-9]{3})/$', user_views.student_profile, name="student"),

]