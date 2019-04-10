
from django.urls import path
from apps.User.views import LoginView

app_name = '[User]'
urlpatterns = [
    path('login', LoginView.as_view(), name='login'),

]
