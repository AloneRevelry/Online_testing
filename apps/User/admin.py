from django.contrib import admin
from apps.User.models import StudentInfo,TeacherInfo

# Register your models here.
admin.site.register(StudentInfo)
admin.site.register(TeacherInfo)
