# -!- coding: utf-8 -!-
__author__ = 'Hunter'

from win32com.client import Dispatch
import win32com.client
import time
excel =  win32com.client.Dispatch('Excel.Application')
excel.Visible = -1
myBook = excel.Workbooks.Open(r'C:\Users\Hunter\PY\2018.xlsx')
mySheet = myBook.Worksheets("1")
LastRow = mySheet.usedrange.rows.count
print("have",LastRow,"line")
mySheet.Activate
mySheet.Cells(2,2).Value=r"测试用"

#get value
aCellValue = mySheet.Cells(2,3).Value
print(aCellValue)
#save
myBook.save
#quit
myBook.close
