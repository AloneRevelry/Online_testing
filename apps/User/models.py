from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    sip = models.CharField(max_length=20, blank=True, null=True)
    submittime = models.DateField(blank=True, null=True)
    is_teacher = models.BooleanField(blank=True, null=True)
    is_student = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'userinfo'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
