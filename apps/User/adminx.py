import xadmin
from apps.User.models import Student, Teacher, User, Class
from apps.Student.models import Files
from xadmin import views
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(label="Password",
        help_text=("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = User
        fields = '__all__'

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""


    password1 = forms.CharField(
        label="密码",
        strip=False,
        widget=forms.PasswordInput,
        help_text="输入密码"
    )
    password2 = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput,
        strip=False,
        help_text="请再次输入密码，确保两次输入一致",
    )
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'user_type', 'is_staff')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.save()

        #if user.user_type == 'teacher':
        #     Student.objects.create(studentname=user.last_name + user.first_name, user_id_id=user.id, teacher_id=12)
        # else:
        #    Teacher.objects.create(teachername=user.last_name + user.first_name, user_id_id=user.id)

        # if commit:
        #     user.save()


        return user


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "上机考试系统后台管理"  # 设置站点标题
    site_footer = "https://github.com/AloneRevelry/Online_testing"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

    # 自定义菜单
    def get_site_menu(self):
        return [
                {
                    'title': '师生信息表',
                    'perm': self.get_model_perm(User, 'view'),
                    'menus': (
                        {
                            'title': '学生信息',
                            'perm': self.get_model_perm(User, 'view'),
                            'url': self.get_model_url(Student, 'changelist')
                                   
                        },
                        {
                            'title': '教师信息',
                            'perm': self.get_model_perm(User, 'view'),
                            'url': self.get_model_url(Teacher, 'changelist')

                        },
                        {
                            'title': '班级信息',
                            'perm': self.get_model_perm(User, 'view'),
                            'url': self.get_model_url(Class, 'changelist')

                        },

                        )

                },

        ]


class CustomAdmin(object):
    list_per_page = 10  # 指定每页显示10条数据
    list_display = ['username', 'get_name', 'is_staff', 'user_type']

    def get_name(self, obj):
        return '%s' % obj.last_name + obj.first_name

    get_name.short_description = '姓名'

    def get_model_form(self, **kwargs):
        if self.org_obj is None:
            self.form = UserCreationForm
        else:
            self.form = UserChangeForm
        return super(CustomAdmin, self).get_model_form(**kwargs)


class StudentAdmin(object):
    list_per_page = 10  # 指定每页显示10条数据
    list_display = ['user_id', 'studentname', 'sip', 'submittime', 'examname', 'Class']

class FilesAdmin(object):
    list_per_page = 10  # 指定每页显示10条数据
    list_display = ['Filename', 'Filetime', 'Filesize', 'student']


class ClassAdmin(object):
    list_per_page = 10
    list_display = ['classname', 'exam_flag']


class TeacherAdmin(object):
    list_per_page = 10  # 指定每页显示10条数据
    list_display = ['user_id', 'teachername', 'Class']


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(Student, StudentAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(User, CustomAdmin)
xadmin.site.register(Files, FilesAdmin)
xadmin.site.register(Class, ClassAdmin)