
from django.urls import path
from apps.Teacher.views import *

app_name = '[Teacher]'
urlpatterns = [
    path('teacher', TeacherView.as_view(), name='teacher'),
    path('teacher/logout', logout_view),
    path('teacher/unlockip', UnlockIpView.as_view(), name='unlockip'),
    path('teacher/fileupload', FileUpload.as_view(), name='fileupload'),
    path('teacher/filedownload', FileDownload.as_view(), name='filedownload'),

]
