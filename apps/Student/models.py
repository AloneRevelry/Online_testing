from django.db import models
from apps.User.models import Student

# Create your models here.
class Files(models.Model):
    # 文件名
    Filename = models.CharField(max_length=100, verbose_name='文件名')
    # 文件的二进制内容
    Filedata = models.BinaryField(max_length=max, verbose_name='文件内容')
    # 文件大小
    Filesize = models.CharField(max_length=100, verbose_name='文件大小')
    # 文件上传时间
    Filetime = models.DateTimeField(auto_now=True, verbose_name='上传时间')
    # 与学生一对多关联
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='学号')

    class Meta:
        db_table = 'student_file'
        verbose_name = '提交文件信息'
        verbose_name_plural = verbose_name
