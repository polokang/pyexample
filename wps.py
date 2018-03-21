from win32com.client import Dispatch
import win32com.client
import time
excel =  win32com.client.Dispatch('Excel.Application')
excel.Visible = -1
myBook = excel.Workbooks.Open(r'd:\320.xls')
mySheet = myBook.Worksheets("1")
row = mySheet.usedrange.rows.count
col = mySheet.usedrange.columns.count
print("have",row,"line")
print("have",col,"col")

i = 2
line = ""
while i <= row:
    j = 1
    while j <= col:
        # print(i-1, '',mySheet.Cells(i,j).Value)
        line += str(mySheet.Cells(i, j).Value) + " "
        j += 1
    print(line)
    line = ""
    i += 1


# mySheet.Activate
# mySheet.Cells(2,2).Value=r"测试用"

#get value
# aCellValue = mySheet.Cells(2,3).Value
# print(aCellValue)
print("............done.")


reSheet = myBook.Worksheets("2")
# reSheet.Activate
reSheet.Cells(2,2).Value = r"测试"
#save
myBook.save

#quit
# myBook.close