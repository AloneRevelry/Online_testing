from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from utils.mixin import LoginRequiredMixin
from django.contrib.auth import logout
from django.http import StreamingHttpResponse
from django.contrib import messages
import os
from apps.User.models import Student
from apps.Student.models import Files

studentname = ''

class StudentView(LoginRequiredMixin, View):

    def get(self, request):
        global studentname
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
            size = '%skb' % str(file.size/1000)
            student = Student.objects.get(studentname=studentname)
            student_file = Files.objects.create(Filename=file.name,
                                                Filesize=size,
                                                Filedata=file.read(),
                                                student=student
                                                )
            student_file.save()

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


class Download(LoginRequiredMixin, View):
    def get(self, request):

        filepath = '/home/alonerevelry/Online_testing/apps'
        global files
        if files:
            files = []

        def get_file(filepath, files):
            for file in os.listdir(filepath):
                file_path = os.path.join(filepath, file)
                if os.path.isdir(file_path):
                    get_file(file_path, files)
                else:
                    filename = file.split('.')[0]
                    filesize = os.path.getsize(file_path)/1000
                    files.append({
                        'filename': filename,
                        'filepath': file_path,
                        'file': file,
                        'filesize': float(filesize),
                    })
        get_file(filepath, files)

        return render(request, 'Student/student_download.html', {
            'files': files,
            'studentname': studentname,
        })

def download_file(request):
    global files
    id = int(request.GET.get('id'))
    file = files[id-1]
    response = StreamingHttpResponse(readFile(file['filepath']))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file['file'])
    return response


def readFile(filename, chunk_size=512):
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


class Fileinfo(LoginRequiredMixin, View):
    def get(self, request):
        studentname = request.COOKIES.get('studentname')
        studentname = studentname.encode("iso-8859-1").decode('utf8')
        student = Student.objects.get(studentname=studentname)
        files = student.files_set.all()
        return render(request, 'Student/student_fileinfo.html', {'files': files})


class Filedata(LoginRequiredMixin, View):

    def get(self, request):
        id = int(request.GET.get('id'))
        file = Files.objects.get(id=id)
        data = file.Filedata.decode(encoding='utf-8')
        return render(request, 'Student/student_filedata.html', {'data': data,
                                                             'filename': file.Filename,
                                                             })