from django.shortcuts import render, redirect
from django.views.generic import View
from utils.mixin import LoginRequiredMixin
from apps.User.models import User
from django.contrib.auth import logout

class StudentView(LoginRequiredMixin, View):

    def get(self, request):

        studentname = request.COOKIES.get('studentname')
        studentname = studentname.encode("iso-8859-1").decode('utf8')
        return render(request, 'Student/student_main.html', {'studentname': studentname})


    def post(self, request):
        pass


def logout_view(request):
    logout(request)

    return redirect('/login')
