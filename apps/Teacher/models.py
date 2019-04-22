from django.db import models
from apps.User.models import Teacher
from django.utils import timezone

# Create your models here.


class Examinfo(models.Model):
    Examstatus_choices =[
        (-1, '已结束'),
        (0, '未开始'),
        (1, '已开始')
    ]
    Examtitle = models.CharField(default='', max_length=50, verbose_name='考试名称')
    Examstarttime = models.DateTimeField(verbose_name='考试开始时间')
    is_auto = models.BooleanField(default=False, verbose_name='自动开始')
    Examstatus = models.IntegerField(default=0, choices=Examstatus_choices, verbose_name='考试状态')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='教师编号')

    class Meta:
        db_table = 'teacher_examinfo'
        verbose_name = '考试信息'
        verbose_name_plural = verbose_name