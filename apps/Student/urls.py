
from django.urls import path
from apps.Student.views import *

app_name = '[Student]'
urlpatterns = [
    path('student', StudentView.as_view(), name='student'),
    path('student/logout', logout_view),
    path('student/download', Download.as_view(), name='download'),
    path('student/download_file', download_file, name='download_file'),
    path('student/fileinfo', Fileinfo.as_view(), name='fileinfo'),
    path('student/fileinfo/filedata', Filedata.as_view(), name='filedata'),
]
