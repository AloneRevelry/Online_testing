
from django.urls import path
from apps.Student.views import *

app_name = '[Student]'
urlpatterns = [
    path('student', StudentView.as_view(), name='student'),
    path('student/logout', logout_view),
    path('student/download', download_view),
    path('student/download_file', download_file, name='download_file')
]
