from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from apps.User.models import User, Student, Class
from apps.Teacher.models import Examinfo
import os
import re
from django.contrib import messages
from django.http import StreamingHttpResponse
import zipfile
from utils.mixin import LoginRequiredMixin
from datetime import datetime
import xlrd


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
            messages.success(request, 'ip解除成功')
            return redirect('Teacher:unlockip')
        except:
            messages.error(request, '不存在该生请确定输入正确学号')
            return redirect('Teacher:unlockip')


class FileUpload(LoginRequiredMixin, View):
    def get(self, request):
        username = request.COOKIES.get('username')
        exams = User.objects.get(username=username).teacher.examinfo_set.filter(Examstatus=0)
        return render(request, 'Teacher/teacher_fileupload.html', {'exams': exams})

    def post(self, request):
        file = request.FILES.get('upload')
        if not file:
            messages.warning(request, '请选择上传文件')
            return redirect('Teacher:fileupload')
        else:
            username = request.COOKIES.get('username')
            examtitle = request.POST.get('examtitle')
            teacher = User.objects.get(username=username).teacher

            classid = str(teacher.Class.id)
            path = '/home/alonerevelry/Online_testing_file/Teacher/%s' % classid
            if not os.path.exists(path):
                os.mkdir(path)
            path = path + '/upload'
            if not os.path.exists(path):
                os.mkdir(path)
            path = path + '/%s' % examtitle
            if not os.path.exists(path):
                os.mkdir(path)
            content = open('%s/%s' % (path, file.name), 'wb+')
            for chunk in file.chunks():
                content.write(chunk)
            content.close()
            messages.success(request, '上传成功')
            return redirect('Teacher:fileupload')


class FileDownload(LoginRequiredMixin, View):

    def get(self, request):
        username = request.COOKIES.get('username')
        teacher = User.objects.get(username=username).teacher
        exam = teacher.examinfo_set.get(Examstatus=1)
        classid = str(teacher.Class.id)
        filepath = '/home/alonerevelry/Online_testing_file/Student/%s/%s' % (classid, exam.Examtitle)
        path = '/home/alonerevelry/Online_testing_file/Teacher/%s/download' % classid
        if not os.path.exists(path):
            os.mkdir(path)
        path = path + '/%s' % username
        if not os.path.exists(path):
            os.mkdir(path)
        file_name = '%s.zip' % username
        file = path+'/%s' % file_name
        z = zipfile.ZipFile(file, 'w')
        pre_len = len(os.path.dirname(filepath))
        for parent, dirnames, filenames in os.walk(filepath):
            for f in filenames:
                path = os.path.join(parent, f)
                arname = path[pre_len:].strip(os.path.sep)
                z.write(path, arname)
        z.close()

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


class NewExamView(LoginRequiredMixin, View):
    def get(self, request):
        nowtime = datetime.now()
        return render(request, 'Teacher/teacher_newexam.html', {'nowtime': nowtime})


    def post(self, request):
        username = request.COOKIES.get('username')
        Examtitle = request.POST.get('Examtitle')
        Examstarttime = request.POST.get('Examstarttime')
        is_auto= bool(request.POST.get('is_auto'))
        Examstarttime = re.match('(.+) ([\u4e00-\u9fa5]+)(\d+)点(\d+)', Examstarttime)
        ymd = Examstarttime.group(1)
        segement = Examstarttime.group(2)
        hour = int(Examstarttime.group(3))
        minute = Examstarttime.group(4)
        if segement == '下午' or segement == '晚上':
            if hour != 12:
                hour += 12
        elif segement == '凌晨' and hour == 12:
            hour = 0
        if hour < 10:
            hour = '0' + str(hour)
        else:
            hour = str(hour)
        Examstarttime = '%s %s:%s:%s' % (ymd, hour, minute, '00')
        teacher = User.objects.get(username=username).teacher
        Examinfo.objects.create(Examtitle=Examtitle, Examstarttime=Examstarttime,
                                       is_auto=is_auto,
                                       teacher=teacher)


        messages.success(request, '考试创建成功')
        return redirect('Teacher:newexam')


class StartExamView(LoginRequiredMixin, View):
    def get(self, request):
        username = request.COOKIES.get('username')
        exams = User.objects.get(username=username).teacher.examinfo_set.all()
        return render(request, 'Teacher/teacher_startexam.html', {'exams': exams})

    def post(self, request):
        id = request.POST.get("id")
        exam = Examinfo.objects.get(id=id)
        if exam.Examstatus == 1:
            messages.error(request, '考试已开始请勿重复开启')
            return redirect('[Teacher]:startexam')

        now = datetime.now()
        if exam.Examstarttime > now:

            minute = (exam.Examstarttime - now).seconds / 60
            if minute > 15:
                messages.warning(request, '请在开始时间前15分内开启考试')
                return redirect('Teacher:startexam')
        else:
            messages.error(request, '考试开始时间已过')
            return redirect('Teacher:startexam')
        exam.Examstatus = 1
        exam.save()
        Class = exam.teacher.Class
        Class.exam_flag = True
        Class.save()
        students = Student.objects.filter(Class=Class)
        for student in students:
            student.examname = exam.Examtitle
            student.save()
        messages.success(request, '考试开启成功')
        return redirect('Teacher:startexam')


class EndExamView(LoginRequiredMixin, View):
    def get(self, request):
        username = request.COOKIES.get('username')
        exams = User.objects.get(username=username).teacher.examinfo_set.all()
        return render(request, 'Teacher/teacher_endexam.html', {'exams': exams})

    def post(self, request):
        id = request.POST.get("id")
        exam = Examinfo.objects.get(id=id)
        if exam.Examstatus == 0:
            messages.error(request, '考试未开启请先开启考试')
            return redirect('Teacher:endexam')
        elif exam.Examstatus == -1:
            messages.error(request, '考试已结束请勿重复操作')
            return redirect('Teacher:endexam')

        exam.Examstatus = -1
        exam.save()
        Class = exam.teacher.Class
        Class.exam_flag = False
        Class.save()
        messages.success(request, '考试关闭成功')
        return redirect('Teacher:endexam')


class ImportStudentsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'Teacher/teacher_importstudents.html')

    def post(self, request):
        file = request.FILES.get('upload')
        if not file:
            messages.warning(request, '请选择上传文件')
            return redirect('Teacher:importstudents')
        else:
            file_type = file.name.split('.')[-1]
            if file_type in ['xlsx', 'xls']:

                path = '/home/alonerevelry/Online_testing_file/temp'
                if not os.path.exists(path):
                    os.mkdir(path)
                filepath = '%s/%s' % (path, file.name)
                content = open(filepath, 'wb+')
                for chunk in file.chunks():
                    content.write(chunk)
                content.close()
                file = xlrd.open_workbook(filepath)
                sheet = file.sheets()[0]
                rows = sheet.nrows
                for i in range(1, rows):
                    username = int(sheet.cell(i, 0).value)
                    studentname = sheet.cell(i, 1).value
                    classname = sheet.cell(i, 2).value
                    user = User.objects.create_user(username=username, password=studentname)
                    user.save()
                    C = Class.objects.get(classname=classname)
                    student = Student.objects.create(studentname=studentname,
                                                     user_id=user,
                                                     Class=C)
                    student.save()

                os.remove(filepath)

                messages.success(request, '信息导入成功')
                return redirect('Teacher:importstudents')
            else:
                messages.error(request, '不是excel文件,请重新选择文件')
                return redirect('Teacher:importstudents')


