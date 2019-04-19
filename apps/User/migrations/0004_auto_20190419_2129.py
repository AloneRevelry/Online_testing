# Generated by Django 2.2 on 2019-04-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_student_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('student', '学生'), ('teacher', '教师')], default='student', max_length=20, verbose_name='用户类型'),
        ),
    ]
