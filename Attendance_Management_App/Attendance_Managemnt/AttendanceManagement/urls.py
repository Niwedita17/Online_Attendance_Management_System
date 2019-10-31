from django.conf.urls import url
from . import views as user_views
from django.contrib.auth import views as auth_views

app_name = 'AttendanceManagement'

urlpatterns = [
    url(r'^$', user_views.index, name='index'),
    #127.0.0.1/attendance/
    url(r'^student/(?P<sid>[0-9]{2}[A-Z]{2}[0-9]{3})/$', user_views.student_profile, name="student"),
    url(r'^student/signup/(?P<sid>[0-9]{2}[A-Z]{2}[0-9]{3})/$', user_views.studentprofile, name="studentSignup"),
    url(r'^faculty/(?P<fid>F[0-9]{2}[A-Z]{2}[0-9]{3})/$', user_views.faculty_profile, name="faculty"),
    url(r'^faculty/signup/(?P<fid>F[0-9]{2}[A-Z]{2}[0-9]{3})/$', user_views.facultyprofile, name="facultySignup"),
    url(r'^courseArchive/$', user_views.course_archive, name='course_archive'),
    url(r'^course/(?P<cid>[A-Z]{2}[0-9]{3})/$', user_views.course_detail, name='course_detail'),
    url(r'^view/$', user_views.view_attendance, name='view'),
    url(r'^give/$', user_views.give_attendance, name='give'),
    url(r'^add_course/$', user_views.give_attendance, name='give'),
    #url(r'^student/(?P<sid>[0-9]{2}[A-Z]{2}[0-9]{3})/register/$', user_views.student_registration, name='student_registration'),
    #url(r'^student/(?P<sid>[0-9]{2}[A-Z]{2}[0-9]{3})/register/$', user_views.student_registration, name='student_registration'),
    #url(r'^student/(?P<sid>[0-9]{2}[A-Z]{2}[0-9]{3})/(?P<cid>[A-Z]{2}[0-9]{3})/$', user_views.student_attendance, name='student_attendance'),
    #url(r'^student/(?P<sid>[0-9]{2}[A-Z]{2}[0-9]{3})/(?P<cid>[A-Z]{2}[0-9]{3})/^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}/$', user_views.reason_for_absence,
     #   name='reason_for_absence'),
    #url(r'^student/(?P<sid>[0-9]{2}[A-Z]{2}[0-9]{3})/register/$', user_views.available_courses, name='available_courses'),
]