#encoding=utf-8
#
# 此模块作为处理excel表格,返回[[{},{}],[{},{}]]格式返回值
# 
import sys,xlrd
from config import table_thead

reload(sys)
sys.setdefaultencoding('utf-8')

class Handle_excel:

    def __init__(self,excel,cur):
        self.excel = excel
        self.cur = cur

    def open_excel(self):
        workbook = xlrd.open_workbook(self.excel)
        try:
            selectsheet = workbook.sheets()[0]
        except Exception as error:
            print "选中表格sheet失败,处理文件中止."
            print error
        # 返回选中sheet
        return selectsheet

    def handle_excel(self):
        exc_make = self.open_excel()        # 创建被处理的excel sheet
        num_rows = exc_make.nrows           # sheet所有行数
        num_cols = exc_make.ncols           # sheet所有列数
        table_key = table_thead[self.cur]   # 一个列表包含表中所有的键名
        res = []

        for rown in range(1,num_rows):
            tmp = {}
            for coln in range(1,num_cols):
                cell = exc_make.cell_value(rown,coln)
                tmp[table_key[coln-1]] = cell
            print tmp
            res.append(tmp)
            print res
        return res











# class Handle_excel:

#     def __init__(self,excel='excel.xlsx',colname_index=0,sheet_index=0):
#         self.excel = excel
#         self.colname_index = colname_index
#         self.sheet_index = sheet_index        

#     # 打开一个excel,并返回一个列表，内每行数据用字典表示  [{'0行列1':'xxx','0行列2':'xxx'},{'1行列1':'xxx','1行列2':'xxx'}]
#     def excel_result(self):
#         try:
#             data = xlrd.open_workbook(self.excel)
#         except Exception as e:
#             print str(e)
        
#         table = data.sheets()[self.sheet_index]  #定位到某个sheet
#         n_rows = table.nrows  #行数
#         n_cols = table.ncols  #列数
#         # colnames = table.row_values(self.colname_index)   #取出来第一行的数据(即列名)
        
#         colnames = []
#         for coln in range(n_cols):
#             cell = table.cell_value(0,coln)
#             colnames.append(table.cell_value(0,coln))
            

#         print colnames
#         res = []
#         for row_num in range(1,n_rows):  # 遍历每一行的数据
#             row = table.row_values(row_num)  # 取出来一整行的值[]
#             if row:
#                 tmp = {}
#                 for i in range(len(colnames)):
#                     tmp[colnames[i]] = row[i]
#                     # {'列1':'xxx','列2':'xxx'}
#                 res.append(tmp)
#                 # [{'列1':'xxx','列2':'xxx'},{'列1':'xxx','列2':'xxx'}] 每一个字典代表一行的数据
#         return res

#     def allowed_type(self):
#         ALLOWED_EXTENSIONS = ['xlsx', 'xls']
#         f_type = self.excel.split('.')[-1]
#         # print f_type
#         if f_type in ALLOWED_EXTENSIONS:
#             return True
#         else:
#             return False

if __name__ == '__main__':
    test = Handle_excel(excel='E:\\Git\\task_draft\\CMDB\\mine\\vm_assets.xlsx')
    print test.excel_result()
    print test.allowed_type()