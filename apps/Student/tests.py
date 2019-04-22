from django.test import TestCase

import xlrd
file = xlrd.open_workbook('/home/alonerevelry/文档/test.xlsx')
s = file.sheets()[0]
r = s.nrows
c = s.ncols
for i in range(1, r):
    text = ''
    for j in range(c):
        text += str(s.cell(i, j).value)
    print(text)
