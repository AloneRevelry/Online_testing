from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth import login, authenticate
from xadmin import views


class LoginView(View):

    '''登录'''
    def get(self, request):

        return render(request, 'User/login.html')

    def post(self, request):
        '''登录校验'''
        # 接收数据
        figure = request.POST.get('figure')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 业务处理：登录校验
        user = authenticate(username=username, password=password)
        if user is not None:
            # 用户名密码正确
            # 记录用户的登录状态
            login(request, user)
            #跳转到相应用户的首页
            if figure == "1":
                if user.is_student == True:
                    # 跳转到学生的首页
                    return redirect(reverse('figure1:index'))
                else:
                    return render(request, 'User/login.html', {'errmsg': '您不是学生,请重新选择您的登录入口'})

            elif figure == "2":
                if user.is_teacher == True:
                    # 跳转到教师的首页
                    return redirect(reverse('figure2:index'))
                else:
                    return render(request, 'User/login.html', {'errmsg': '你不是教师哦,请选择学生登录入口'})
            else:
                if user.is_staff == True:
                    # 跳转到管理员的首页

                    return views.LoginView.as_view()(request)
                else:
                    return render(request, 'User/login.html', {'errmsg': '您没有管理权限'})

        else:
            # 用户名或密码错误
            return render(request, 'User/login.html', {'errmsg': '用户名密码错误'})

        # 返回应答
