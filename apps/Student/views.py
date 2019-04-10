from django.shortcuts import render, redirect, reverse
from django.views.generic import View


class StudentView(View):

    def get(self, request):
        if request.user.is_authenticated:
            studentname = request.COOKIES.get('studentname')
            studentname = studentname.encode("iso-8859-1").decode('utf8')
            return render(request, 'Student/student_head.html', {'studentname': studentname})
        else:
            return redirect('/login')

    def post(self, request):
        pass