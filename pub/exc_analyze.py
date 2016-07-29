#encoding=utf-8
#
# 此模块作为处理excel表格,返回[{},{},{},{}]格式返回值
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
            res.append(tmp)
        return res                          # 返回[{},{},{},{}]格式

if __name__ == '__main__':
    pass