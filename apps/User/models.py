from django.db import models


class StudentInfo(models.Model):
    sid = models.IntegerField()
    sname = models.CharField(max_length=20)
    sip = models.CharField(max_length=20)
    submittime = models.DateField()

    class Meta:
        db_table = 'studentinfo'
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name


class TeacherInfo(models.Model):
    tid = models.IntegerField()
    tname = models.CharField(max_length=20)
    tpassword = models.CharField(max_length=20)
    admin_flag = models.BooleanField(default=False)

    class Meta:
        db_table = 'teacherinfo'
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name
