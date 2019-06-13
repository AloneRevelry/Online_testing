from apps.Teacher.views import exam_list
import datetime

def task():

    now = datetime.datetime.now()
    for exam in exam_list:
        if exam.is_auto:
            time = exam.Examstarttime
            if now - time <= 60:
                time.Examstatus = 1
                time.save()

