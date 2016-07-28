#encoding=utf-8
#

from pub import DB,Handle_excel
from config import db_config, table_thead, excel_thead
# print db_config

db = DB(host=db_config['host'], mysql_user=db_config['user'], mysql_pass=db_config['passwd'], mysql_db=db_config['db'])

class User:

    def __init__(self, cur='user'):
        self.cur = 'user'

    def user_res(self, sql):
        try:
            res = db.execute(sql)
        except Exception as error:
            print '服务器出错,获取用户失败.'
            print error
            return False
        return res

    def user_add(self, sql):
        try:
            db.execute(sql)
        except Exception as error:
            print '服务器出错,添加用户失败.'
            print error
            return False
        return True

    def user_delete(self, sql):
        try:
            db.execute(sql)
        except Exception as error:
            print '服务器出错,删除用户失败.'
            print error
            return False
        return True

    def user_update(self, sql):
        try:
            db.execute(sql)
        except Exception as error:
            print '服务器出错,用户信息更新失败.'
            print error
            return False
        return True

    def user_import(self,excel,cur):
        instance = Handle_excel(excel=excel,cur=cur)
        table_res = instance.handle_excel()
        sql = 'insert into user (username,password,role,email) values ("%s","%s","%s","%s")'
        for data in table_res:
            tmp = []
            for key in table_thead[cur]:
                tmp.append(data[key])
            # print tmp
            insert_sql = sql % tuple(tmp)
            # print insert_sql
            db.execute(insert_sql)


        

    def user_export(self):
        sql = "select username,password,role,email from user"
        dbres = db.execute(sql)                 # 从数据库获取数据格式为({},{})
        export_res = []                         # 定义获取导出数据格式[[],[]]
        exc_thead = excel_thead[self.cur]       # 引入excel表头文件
        tab_thead = table_thead[self.cur]       # 引入db表头文件
        export_res.append(exc_thead)
        for i in range(len(dbres)):
            tmp = [i+1]
            for thead in tab_thead:
                tmp.append(dbres[i][thead])
            export_res.append(tmp)
        # print export_res
        return export_res
            



class VM_assets:

    def __init__(self):
        pass

    def vmassets_res(self, sql):
        try:
            res = db.execute(sql)
        except Exception as error:
            print 'Get vm assets failed.'
            print error
            return False
        return res

    def vmassets_add(self, sql):
        try:
            db.execute(sql)
        except Exception as error:
            print 'Add vm assets failed.'
            print error
            return False
        print '资源添加成功'
        return True

    def vmassets_delete(self, sql):
        try:
            db.execute(sql)
        except Exception as error:
            print 'Delete vm assets failed.'
            print error
            return False
        return True

    def vmassets_update(self, sql):
        try:
            db.execute(sql)
        except Exception as error:
            print 'Update vm assets failed.'
            print error
            return False
        return True
