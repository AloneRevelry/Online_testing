
from django.urls import path
from apps.Teacher.views import *

app_name = '[Teacher]'
urlpatterns = [
    path('teacher', TeacherView.as_view(), name='teacher'),
    path('teacher/logout', logout_view),
    path('teacher/unlockip', UnlockIpView.as_view(), name='unlockip'),
    path('teacher/fileupload', FileUpload.as_view(), name='fileupload'),
    path('teacher/filedownload', FileDownload.as_view(), name='filedownload'),
    path('teacher/newexam', NewExamView.as_view(), name='newexam'),
    path('teacher/startexam', StartExamView.as_view(), name='startexam'),
    path('teacher/endexam', EndExamView.as_view(), name='endexam'),
    path('teacher/importstudents', ImportStudentsView.as_view(), name='importstudents'),
    path('teacher/studentinfo', StudentInfoView.as_view(), name='studentinfo'),
    path('teacher/showexamstatus', ShowExamStatus.as_view(), name='showexamstatus'),
    path('teacher/exportstudents', ExportStudentView.as_view(), name='exportstudents'),
    path('teacher/sendmsg', SendMsgView.as_view(), name='sendmsg'),
    path('teacher/clean', CleanView.as_view(), name='clean'),

]
