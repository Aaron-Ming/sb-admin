#encoding=utf-8
#

from pub import DB
from config import db_config
# print db_config

db = DB(host=db_config['host'], mysql_user=db_config['user'], mysql_pass=db_config['passwd'], mysql_db=db_config['db'])

class User:

    def __init__(self):
        pass

    def user_res(self, sql):
        try:
            res = db.execute(sql)
        except Exception as error:
            print 'Get user failed.'
            print error
            return False
        return res

    def user_add(self, sql):
        try:
            db.execute(sql)
        except Exception as error:
            print 'Add user failed.'
            print error
            return False
        return True

    def user_delete(self, sql):
        try:
            db.execute(sql)
        except Exception as error:
            print 'Delete user failed.'
            print error
            return False
        return True

    def user_update(self, sql):
        try:
            db.execute(sql)
        except Exception as error:
            print 'Update user failed.'
            print error
            return False
        return True

    def user_import(self):
        pass

    def user_export(self):
        pass



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
