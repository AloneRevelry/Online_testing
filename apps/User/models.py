from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_type_choices = (
        ('student', '学生'),
        ('teahcer', '教师')
    )
    is_staff_choices = (
        (False, '非管理员'),
        (True, '管理员')
    )
    user_type = models.CharField('用户类型', max_length=20, choices=user_type_choices, default='student')
    is_staff = models.BooleanField('职员状态', choices=is_staff_choices, default=False)

    class Meta:
        verbose_name = '用户列表'
        verbose_name_plural = verbose_name


class Student(models.Model):

    studentname = models.CharField(max_length=20, verbose_name='姓名')
    sip = models.CharField(max_length=20, blank=True, null=True, verbose_name='绑定ip地址')
    submittime = models.DateField(blank=True, null=True, verbose_name='提交时间')
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='学号')

    class Meta:
        db_table = 'student_info'
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name


class Teacher(models.Model):

    user_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='教职工编号')
    teachername = models.CharField(max_length=20, verbose_name='姓名')

    class Meta:
        db_table = 'teacher_info'
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name