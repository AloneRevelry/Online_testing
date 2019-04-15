
from django.urls import path
from apps.Teacher.views import TeacherView, logout_view

app_name = '[Teacher]'
urlpatterns = [
    path('teacher', TeacherView.as_view(), name='teacher'),
    path('teacher/logout', logout_view),
]
