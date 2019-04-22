from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth import login, authenticate
from xadmin import views
from apps.User.models import Student, User
from apps.Teacher.models import Examinfo



class LoginView(View):

    '''登录'''
    def get(self, request):
        checked = ''
        if 'username1' in request.COOKIES:
            username1 = request.COOKIES['username1']
            checked = 'checked'
        else:
            username1 = ''
        if 'username2' in request.COOKIES:
            username2 = request.COOKIES['username2']
            checked = 'checked'
        else:
            username2 = ''
        if 'username3' in request.COOKIES:
            username3 = request.COOKIES['username3']
            checked = 'checked'
        else:
            username3 = ''

        return render(request, 'User/login.html', {
            'username1': username1,
            'username2': username2,
            'username3': username3,
            'checked': checked,
        })

    def post(self, request):
        '''登录校验'''
        # 接收数据
        figure = request.POST.get('figure')
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        # 业务处理：登录校验
        user = authenticate(username=username, password=password)
        if user is not None:

            # 用户名密码正确
            #跳转到相应用户的首页
            if figure == "1":
                if user.user_type == 'student':

                    Class = User.objects.get(username=username).student.Class

                    if not Class.exam_flag:
                        return render(request, 'User/login.html', {'errmsg': '考试未开始,请稍等'})
                    ip = request.META['REMOTE_ADDR']
                    if user.student.sip == None:
                        astudent = Student.objects.get(studentname=user.student.studentname)
                        astudent.sip = ip
                        astudent.save()
                    else:
                        if user.student.sip != ip:
                            return render(request, 'User/login.html', {'errmsg': '此用户已在其他电脑登录'})

                    # 记录用户的登录状态
                    login(request, user)
                    # 跳转到学生的首页
                    name = user.student.studentname
                    next_url = request.GET.get('next', reverse('Student:student'))
                    response = redirect(next_url)
                    response.set_cookie("studentname", bytes(name, 'utf8').
                                        decode('ISO-8859-1'), max_age=7 * 24 * 3600)
                    response.set_cookie('username', username)
                    if remember == 'rm':
                        response.set_cookie("username1", username, max_age=7*24*3600)
                    else:
                        if 'username1' in request.COOKIES:
                            response.delete_cookie('username1')
                    return response
                else:
                    return render(request, 'User/login.html', {'errmsg': '您不是学生,请重新选择您的登录入口'})

            elif figure == "2":
                if user.user_type == 'teacher':

                    # 记录用户的登录状态
                    login(request, user)
                    # 跳转到教师的首页
                    name = user.teacher.teachername
                    next_url = request.GET.get('next', reverse('Teacher:teacher'))
                    response = redirect(next_url)
                    response.set_cookie("teachername", bytes(name, 'utf8').
                                        decode('ISO-8859-1'), max_age=7 * 24 * 3600)
                    response.set_cookie('username', username)
                    if remember == 'rm':
                        response.set_cookie("username2", username, max_age=7 * 24 * 3600)
                    else:
                        if 'username2' in request.COOKIES:
                            response.delete_cookie('username2')

                    return response
                else:
                    return render(request, 'User/login.html', {'errmsg': '你不是教师哦,请选择学生登录入口'})
            else:
                if user.is_staff == True:
                    # 跳转到管理员的首页
                    # 记录用户的登录状态
                    login(request, user)
                    response = views.LoginView.as_view()(request)
                    if remember == 'rm':
                        response.set_cookie("username3", username, max_age=7 * 24 * 3600)
                    else:
                        if 'username3' in request.COOKIES:
                            response.delete_cookie('username3')
                    return response
                else:
                    return render(request, 'User/login.html', {'errmsg': '您没有管理权限'})

        else:
            # 用户名或密码错误
            return render(request, 'User/login.html', {'errmsg': '用户名密码错误'})

        # 返回应答
