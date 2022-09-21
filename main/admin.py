from django.contrib import admin

from main.models import LecturerProfile, User, Student, Lecturer


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'role', 'department']

admin.site.register(User, UserAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'role', 'department']

admin.site.register(Student, StudentAdmin)


class LecturerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'role', 'department']

admin.site.register(Lecturer, LecturerAdmin)



class LecturerProfileAdmin(admin.ModelAdmin):
    list_display = ['lecturer', 'course']

admin.site.register(LecturerProfile, LecturerProfileAdmin)
