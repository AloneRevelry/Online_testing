from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from utils.mixin import LoginRequiredMixin
from django.contrib.auth import logout
from django.http import StreamingHttpResponse
from django.contrib import messages
import os


class StudentView(LoginRequiredMixin, View):

    def get(self, request):

        studentname = request.COOKIES.get('studentname')
        studentname = studentname.encode("iso-8859-1").decode('utf8')
        return render(request, 'Student/student_main.html', {'studentname': studentname})

    def post(self, request):
        file = request.FILES.get('upload')
        if not file:
            messages.warning(request, '请选择上传文件')
            return redirect('/student')
        else:
            studentname = request.COOKIES.get('studentname')
            studentname = studentname.encode("iso-8859-1").decode('utf8')
            path = '/home/alonerevelry/UpFiles/%s' % studentname
            if not os.path.exists(path):
                os.mkdir(path)
            content = open('%s/%s' % (path, file.name), 'wb+')
            for chunk in file.chunks():
                content.write(chunk)
            content.close()
            messages.success(request, '上传成功')
            return redirect('/student')


def logout_view(request):
    logout(request)

    return redirect('/login')

files = []
def download_view(request):

    filepath = '/home/alonerevelry/Online_testing/templates/Student'
    global files
    if files:
        files = []

    for file in os.listdir(filepath):
        file_path = os.path.join(filepath, file)
        files.append({'filename': file, 'filepath': file_path})

    return render(request, 'Student/student_download.html', {'files': files})


def download_file(request):
    global files
    id = int(request.GET.get('id'))
    file = files[id-1]
    response = StreamingHttpResponse(readFile(file['filepath']))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file['filename'])
    return response


def readFile(filename, chunk_size=512):
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break

