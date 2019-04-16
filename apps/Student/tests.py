from django.test import TestCase

import os

def getfile(filepath):
#遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for file in files:
        file_path = os.path.join(filepath, file)
        if os.path.isdir(file_path):
            getfile(file_path)
        else:
            print(file_path)


#递归遍历/root目录下所有文件
#getfile('/home/alonerevelry/Online_testing/templates')
files = [{'filename': 'student_download.html', 'file_path': '/home/alonerevelry/Online_testing/templates/Student/student_download.html'}, {'filename': 'student_main.html', 'file_path': '/home/alonerevelry/Online_testing/templates/Student/student_main.html'}, {'filename': 'student_base.html', 'file_path': '/home/alonerevelry/Online_testing/templates/Student/student_base.html'}]
print(files[0]['filename'])