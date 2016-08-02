#encoding=utf-8
#

from pub import DB,Handle_excel
from config import db_config, table_thead, excel_thead
import copy


db = DB(host=db_config['host'], mysql_user=db_config['user'], mysql_pass=db_config['passwd'], mysql_db=db_config['db'])

class Action:

    def __init__(self):
        pass

    def auth_info(self):
        sql = 'select username,password from user'
        res = db.execute(sql)
        user_info = {}
        for bar in res:
            user_info[bar['username']] = bar['password']
        return user_info        # 返回用户密码{xxx,:xxx, yyy:yyy}


    def get_data(self, sql):
        try:
            res = db.execute(sql)
        except Exception as error:
            print '获取数据失败,请联系管理员.'
            print error
            return False
        return res

    def sql_operation(self, sql,status):
        try:
            db.execute(sql)
        except Exception as error:
            if status == "add":
                print '添加数据失败,请检查填写信息是否冲突.'
            elif status == "update":
                print '数据信息更新失败.'
            elif status == "delete":
                print '删除数据失败.'
            print error
            return False
        return True

    def data_import(self,excel,cur):
        instance = Handle_excel(excel=excel,cur=cur)    # 初始化一个处理excel实例
        table_res = instance.handle_excel()             # 获取excel的数据，格式为[{},{},{}]
        multiple = len(table_thead[cur])                # 拼接%s的倍数 

        first_list = ['%s'] * multiple                  # 
        front_dir = ','.join(first_list)                # 拼接sql前半部分
        second_list = ['"%s"'] * multiple               # 
        back_dir = ','.join(second_list)                # 拼接sql后半部分

        tmp_sql = 'insert into %s (' + front_dir + ') values (' + back_dir + ')'
        tmp = [cur]                                     # 
        for thead in table_thead[cur]:                  # 定义一个临时[],用于存放sql格式化的值
            tmp.append(thead)                           #

        for data in table_res:
            format_val = copy.deepcopy(tmp)
            for key in table_thead[cur]:
                format_val.append(data[key])
            sql = tmp_sql % tuple(format_val)
            db.execute(sql)

    def data_export(self,cur):
        multiple = len(table_thead[cur])               # 拼接%s的倍数 
        join_list = ['%s'] * multiple                  #
        split_str = ','.join(join_list)                # 拼接sql
        tmp_sql = "select " + split_str + " from %s"

        format_val = []
        for thead in table_thead[cur]:
            format_val.append(thead)
        format_val.append(cur)
        sql = tmp_sql % tuple(format_val)
        dbres = db.execute(sql)                 # 从数据库获取数据格式为({},{})
        export_res = []                         # 定义获取导出数据格式[[],[]]
        exc_thead = excel_thead[cur]            # 引入excel表头文件
        tab_thead = table_thead[cur]            # 引入db表头文件
        export_res.append(exc_thead)
        for i in range(len(dbres)):
            tmp = [i+1]
            for thead in tab_thead:
                tmp.append(dbres[i][thead])
            export_res.append(tmp)
        return export_res                       # 返回数据格式[[],[],[]]作为导入excel的数据
            




