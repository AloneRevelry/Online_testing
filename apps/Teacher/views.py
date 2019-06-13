from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from apps.User.models import User, Student, Class
from apps.Teacher.models import Examinfo
import os
import shutil
import re
from django.contrib import messages
from django.http import StreamingHttpResponse
import zipfile
from utils.mixin import LoginRequiredMixin
from datetime import datetime
import xlrd, xlwt

exam_list = []

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
        exam_flag = teacher.Class.exam_flag
        if exam_flag:
            messages.warning(request, '考试尚未结束')
            return redirect('Teacher:teacher')
        classid = str(teacher.Class.id)
        filepath = '/home/alonerevelry/Online_testing_file/Student/%s/%s' % (classid, Class.exam_title)
        path = '/home/alonerevelry/Online_testing_file/Teacher/%s' % classid
        if not os.path.exists(path):
            os.mkdir(path)
        path = path + '/download'
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

        exam = Examinfo.objects.create(Examtitle=Examtitle, Examstarttime=Examstarttime,
                                       is_auto=is_auto,
                                       teacher=teacher)
        exam_list.append(exam)

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
        Class.exam_title = exam.Examtitle
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


class StudentInfoView(LoginRequiredMixin, View):

    def get(self, request):
        username = request.COOKIES.get('username')
        teacher = User.objects.get(username=username).teacher
        students = Student.objects.filter(Class=teacher.Class)
        return render(request, 'Teacher/teacher_studentinfo.html', {'students': students})

    def post(self, request):
        studentid = request.POST.get('studentid')
        studentname = request.POST.get('studentname')
        classname = request.POST.get('class')

        try:
            user = User.objects.create_user(username=studentid, password=studentname)
            user.save()
            C = Class.objects.get(classname=classname)
            student = Student.objects.create(studentname=studentname,
                                             user_id=user,
                                             Class=C)
            student.save()
            messages.success(request, ' 学生添加成功')
        except:
            messages.error(request, '输入信息有误')

        return redirect('Teacher:studentinfo')


class ShowExamStatus(LoginRequiredMixin, View):

    def get(self, request):
        username = request.COOKIES.get('username')
        teacher = User.objects.get(username=username).teacher
        students = Student.objects.filter(Class=teacher.Class)
        login_students = []
        unlogin_students = []
        submit_students = []
        unsubmit_students = []
        login_num = 0
        submit_num = 0
        student_num = len(students)
        lists = []
        for student in students:
            if student.sip:
                login_num += 1
                login_students.append(student)
            else:
                unlogin_students.append(student)

            if student.submittime:
                submit_num += 1
                submit_students.append(student)
            else:
                unsubmit_students.append(student)


        unlogin_num = student_num - login_num
        unsubmit_num = student_num - submit_num
        max_num = max(login_num, unlogin_num, submit_num, unsubmit_num)

        for i in range(max_num):
            a = ' '
            b = ' '
            c = ' '
            d = ' '
            if i+1<=len(login_students):
                a = login_students[i].studentname
            if i+1<=len(unlogin_students):
                b = unlogin_students[i].studentname
            if i+1<=len(submit_students):
                c = submit_students[i].studentname
            if i+1<=len(unsubmit_students):
                d = unsubmit_students[i].studentname

            lists.append([a, b, c, d])

        return render(request, 'Teacher/teacher_showexamstatus.html', {
            'login_num': login_num,
            'unlogin_num': unlogin_num,
            'submit_num': submit_num,
            'unsubmit_num': unsubmit_num,
            'lists': lists,
        })


class ExportStudentView(LoginRequiredMixin, View):
    def get(self, request):
        username = request.COOKIES.get('username')
        teacher = User.objects.get(username=username).teacher
        students = Student.objects.filter(Class=teacher.Class)
        path = '/home/alonerevelry/Online_testing_file/temp/studentinfo.xls'

        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet('sheet1')
        worksheet.write(0, 0, label='学号')
        worksheet.write(0, 1, label='姓名')
        worksheet.write(0, 2, label='最后提交时间')
        worksheet.write(0, 3, label='班级')
        n = 1
        for student in students:
            worksheet.write(n, 0, label=str(student.user_id))
            worksheet.write(n, 1, label=str(student.studentname))
            worksheet.write(n, 2, label=str(student.submittime))
            worksheet.write(n, 3, label=str(student.Class))
            n += 1
        workbook.save(path)
        response = StreamingHttpResponse(self.readFile(path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format('sutdentinfo.xls')
        return response

    def readFile(self, filename, chunk_size=512):
        with open(filename, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break


class SendMsgView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'Teacher/teacher_sendmsg.html')

    def post(self, request):
        username = request.COOKIES.get('username')
        teacher = User.objects.get(username=username).teacher
        Class = teacher.Class
        msg = request.POST.get('msg')
        Class.msg = msg
        Class.save()
        messages.success(request, '消息发送成功')
        return redirect('Teacher:sendmsg')


class CleanView(LoginRequiredMixin, View):

    def get(self, request):
        username = request.COOKIES.get('username')
        user = User.objects.get(username=username)
        if user.is_staff:
            return render(request, 'Teacher/teacher_clean.html')
        else:
            messages.error(request, '您没有清理考试权限')
            return redirect('Teacher:teacher')

    def post(self, request):
        username = request.COOKIES.get('username')
        teacher = User.objects.get(username=username).teacher
        Class = teacher.Class
        classid = str(Class.id)
        if Class.exam_flag:
            messages.error(request, '考试尚未结束,无法清理考试内容')
            return redirect('Teacher:teacher')
        path = '/home/alonerevelry/Online_testing_file/Teacher/%s/download/%s' % (classid, teacher.user_id)
        if not os.path.exists(path):
            messages.error(request, '学生答卷尚未打包,请先打包')
            return redirect('Teacher:teacher')

        shutil.rmtree(path)
        path = '/home/alonerevelry/Online_testing_file/Student/%s' % classid
        shutil.rmtree(path)
        path = '/home/alonerevelry/Online_testing_file/Teacher/%s/upload' % classid
        shutil.rmtree(path)
        path = '/home/alonerevelry/Online_testing_file/temp/studentinfo.xls'
        if os.path.exists(path):
            os.remove(path)
        exams = teacher.examinfo_set.all()
        for exam in exams:
            exam.delete()
        for student in Class.student_set.all():
            student.user_id.delete()

        messages.success(request, '考试清理完成')
        return redirect('Teacher:teacher')


