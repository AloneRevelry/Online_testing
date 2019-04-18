from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout

# Create your views here.
class TeacherView(View):

    def get(self, request):

        return render(request, 'Teacher/teacher_base.html')
    def post(self):
        pass

def logout_view(request):
    logout(request)

    return redirect('/login')
