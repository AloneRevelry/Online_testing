# Generated by Django 2.2 on 2019-04-22 21:35

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(max_length=20, verbose_name='班级名称')),
                ('exam_flag', models.BooleanField(default=False, verbose_name='是否开启考试')),
            ],
            options={
                'verbose_name': '班级信息',
                'verbose_name_plural': '班级信息',
                'db_table': 'class_info',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('student', '学生'), ('teacher', '教师')], default='student', max_length=20, verbose_name='用户类型')),
                ('is_staff', models.BooleanField(choices=[(False, '非管理员'), (True, '管理员')], default=False, verbose_name='职员状态')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户列表',
                'verbose_name_plural': '用户列表',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachername', models.CharField(max_length=20, verbose_name='姓名')),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Class', verbose_name='所属班级')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='教职工编号')),
            ],
            options={
                'verbose_name': '教师信息',
                'verbose_name_plural': '教师信息',
                'db_table': 'teacher_info',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=20, verbose_name='姓名')),
                ('sip', models.CharField(blank=True, max_length=20, null=True, verbose_name='绑定ip地址')),
                ('submittime', models.DateTimeField(blank=True, null=True, verbose_name='提交时间')),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Class', verbose_name='所属班级')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='学号')),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息',
                'db_table': 'student_info',
            },
        ),
    ]
