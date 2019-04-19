from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from apps.User.models import User
import os
from django.contrib import messages
from django.http import StreamingHttpResponse
import zipfile
from utils.mixin import LoginRequiredMixin

# Create your views here.
class TeacherView(LoginRequiredMixin, View):

    def get(self, request):

        return render(request, 'Teacher/teacher_base.html')
    def post(self):
        pass


def logout_view(request):
    logout(request)

    return redirect('/login')


class UnlockIpView(LoginRequiredMixin, View):

    def get(self, request):

        return render(request, 'Teacher/teacher_unlockip.html')

    def post(self, request):
        studentid = request.POST.get('studentid')
        try:
            student = User.objects.get(username=studentid).student
            student.sip = None
            student.save()
            messages = 'ip解除成功'
            return render(request, 'Teacher/teacher_unlockip.html', {'msg': messages, 'color': 'green'})
        except:
            messages = '不存在该生请确定输入正确学号'
            return render(request, 'Teacher/teacher_unlockip.html', {'msg': messages, 'color': 'red'})


class FileUpload(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'Teacher/teacher_fileupload.html')

    def post(self, request):
        file = request.FILES.get('upload')
        if not file:
            messages.warning(request, '请选择上传文件')
            return redirect('/teacher/fileupload')
        else:
            username = request.COOKIES.get('username')
            path = '/home/alonerevelry/Online_testing_file/Teacher/%s' % username
            if not os.path.exists(path):
                os.mkdir(path)
            path = '/home/alonerevelry/Online_testing_file/Teacher/%s/upload' % username
            if not os.path.exists(path):
                os.mkdir(path)
            content = open('%s/%s' % (path, file.name), 'wb+')
            for chunk in file.chunks():
                content.write(chunk)
            content.close()
            messages.success(request, '上传成功')
            return redirect('/teacher/fileupload')

class FileDownload(LoginRequiredMixin, View):

    def get(self, request):
        username = request.COOKIES.get('username')
        filepath = '/home/alonerevelry/Online_testing_file/Student/%s' % username
        path = '/home/alonerevelry/Online_testing_file/Teacher/%s/download' % username
        if not os.path.exists(path):
            os.mkdir(path)
        file_name = 'studentfile.zip'
        file = '/home/alonerevelry/Online_testing_file/Teacher/%s/download/studentfile.zip' % username
        z = zipfile.ZipFile(file, 'w')
        pre_len = len(os.path.dirname(filepath))
        for parent, dirnames, filenames in os.walk(filepath):
            for file in filenames:
                path = os.path.join(parent, file)
                arname = path[pre_len:].strip(os.path.sep)
                z.write(path, arname)
        z.close()

        file = '/home/alonerevelry/Online_testing_file/Teacher/%s/download/studentfile.zip' % username
        response = StreamingHttpResponse(self.readFile(file))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
        return response

    def readFile(self, filename, chunk_size=512):
        with open(filename, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break