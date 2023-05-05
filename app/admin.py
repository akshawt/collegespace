from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

class UserModel(UserAdmin):
    model=CustomUser
    list_display=['username','user_type']

admin.site.register(CustomUser,UserModel)
admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(Attendance_Report)
admin.site.register(StudentResult)
admin.site.register(StudentApplication)




