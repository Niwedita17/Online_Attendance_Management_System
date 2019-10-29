# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.db import models


class CourseAttendance(models.Model):
    sid = models.ForeignKey('StudentInfo', models.DO_NOTHING, db_column='sid', primary_key=True)
    cid = models.ForeignKey('CourseInfo', models.DO_NOTHING, db_column='cid')
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    attendance = models.CharField(max_length=3)
    reason_for_absence = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Course_Attendance'
        unique_together = (('sid', 'cid'),)


class CourseInfo(models.Model):
    cid = models.CharField(primary_key=True, max_length=5)
    cname = models.CharField(max_length=15)
    no_of_classes = models.IntegerField()
    course_plan = models.CharField(max_length=100)
    fid = models.ForeignKey('FacultyInfo', models.DO_NOTHING, db_column='fid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Course_Info'


class CourseRegistration(models.Model):
    sid = models.ForeignKey('StudentInfo', models.DO_NOTHING, db_column='sid', primary_key=True)
    cid = models.ForeignKey(CourseInfo, models.DO_NOTHING, db_column='cid')

    class Meta:
        managed = False
        db_table = 'Course_Registration'
        unique_together = (('sid', 'cid'),)


class FacultyInfo(models.Model):
    fid = models.CharField(primary_key=True, max_length=8, )
    f_fname = models.CharField(max_length=10)
    f_lname = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    area_of_interest = models.CharField(max_length=30)
    btech = models.CharField(max_length=20)
    mtech = models.CharField(max_length=20)
    phd = models.CharField(max_length=20)
    house_no = models.CharField(max_length=10)
    street = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()
    password = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Faculty_Info'


class StudentInfo(models.Model):
    sid = models.CharField(primary_key=True, max_length=7, validators=[
        RegexValidator(
            regex='^[0-9]{2}[A-Z]{2}[0-9]{3}$',
            message='ID should be of form e.g 19CO101',
            code='invalid_studentID'
        ),
    ])
    s_fname = models.CharField(max_length=15)
    s_lname = models.CharField(max_length=15)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=10, validators=[RegexValidator(regex='^[0-9]{10}$'), ])
    degree = models.CharField(max_length=20)
    house_no = models.CharField(max_length=10)
    street = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6, validators=[RegexValidator(regex='^[0-9]{6}$'), ])

    class Meta:
        managed = False
        db_table = 'Student_Info'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
