
from django.urls import path
from apps.Student.views import StudentView

app_name = '[Student]'
urlpatterns = [
    path('student', StudentView.as_view(), name='student'),

]