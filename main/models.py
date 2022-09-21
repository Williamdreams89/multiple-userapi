from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from .managers import UserManager
# from django.contrib.auth.models import GroupManager

class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        LECTURER = 'LECTURER', 'Lecturer'
        STUDENT = 'STUDENT', 'Student'
        HOD = "HEAD OF DEPARTMENT", 'Head of Department'
        HOF = "HEAD OF FACULTY", 'Head of Faculty'

    base_role = Role.STUDENT

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=100, choices=Role.choices)
    department = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "images/")
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role', 'department']

    objects = UserManager()

    



class StudentManager(BaseUserManager):

    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role = User.Role.STUDENT)

class Student(User):
    base_role = User.Role.STUDENT

    students = StudentManager()

    class Meta:
        proxy = True


class LecturerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role = User.Role.LECTURER)

class Lecturer(User):
    base_role = User.Role.LECTURER

    lecturers = LecturerManager()

    class Meta: 
        proxy = True



class LecturerProfile(models.Model):
    lecturer = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)




