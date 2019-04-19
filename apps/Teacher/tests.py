from django.test import TestCase
import zipfile
import os
# Create your tests here.
def readFile(filename, chunk_size=512):
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break

filepath = '/home/alonerevelry/UpFiles'
file_name = '/home/alonerevelry/hh/studentfile.zip'
z = zipfile.ZipFile(file_name, 'w')
pre_len = len(os.path.dirname(filepath))
for parent, dirnames, filenames in os.walk(filepath):
    for file in filenames:
        path = os.path.join(parent, file)
        arname = path[pre_len:].strip(os.path.sep)
        z.write(path, arname)

z.close()
