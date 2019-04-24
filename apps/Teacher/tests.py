import xlwt
workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('sheet1')
worksheet.write(0, 0, label='学号')
worksheet.write(0, 1, label='姓名')
worksheet.write(0, 2, label='最后提交时间')
worksheet.write(0, 2, label='班级')
workbook.save('test.xls')