from django.shortcuts import render, redirect
from django.views.generic import View
from utils.mixin import LoginRequiredMixin


class StudentView(LoginRequiredMixin, View):

    def get(self, request):

        studentname = request.COOKIES.get('studentname')
        studentname = studentname.encode("iso-8859-1").decode('utf8')
        return render(request, 'Student/student_main.html', {'studentname': studentname})


    def post(self, request):
        pass