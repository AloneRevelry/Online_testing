
from django.urls import path
from apps.Student.views import StudentView, logout_view

app_name = '[Student]'
urlpatterns = [
    path('student', StudentView.as_view(), name='student'),
    path('student/logout', logout_view),

]
