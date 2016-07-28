#encoding=utf-8
#

from flask import Flask, redirect, render_template, session, url_for, g, request
import sys,os
from api import User, VM_assets
from pub import Env_check,Handle_excel
from config import app_config
from flask.ext import excel
from pyexcel.ext import xlsx
from werkzeug import secure_filename

reload(sys)
sys.setdefaultencoding('utf-8')


app = Flask(__name__)


@app.route('/vm_assets')
def vm_assets():
    return render_template('vm_assets.html')

@app.route('/user')
def user():
    sql = 'select id,username,password,role,email from user'
    res = User().user_res(sql)
    return render_template('user.html', user_info=res)

@app.route('/user/add', methods=['POST'])
def user_add():
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    role = request.form.get('role', None)
    email = request.form.get('email', None)
    sql = 'insert into user (username,password,role,email) values ("%s","%s","%s","%s")' % (username,password,role,email)
    if User().user_add(sql):
        return 'ok'
    else:
        return 'error'


@app.route('/user/delete', methods=['POST'])
def user_delete():
    userid = request.form.get('id', None)
    sql = 'delete from user where id="%s"' % (userid)
    print 'userid is'+userid
    if User().user_delete(sql):
        return 'ok'
    else:
        return 'error'


@app.route('/user/update', methods=['POST'])
def user_update():
    userid = request.form.get('id', None)
    role = request.form.get('update_role', None)
    password = request.form.get('update_password', None)
    email = request.form.get('update_email', None)
    sql = 'update user set password="%s",role="%s",email="%s" where id="%s"' % (password,role,email,userid)
    print sql
    if User().user_update(sql):
        return 'ok'
    else:
        return 'error'


@app.route("/user/import", methods=['GET', 'POST'])
def upload_file():
    file = request.files['upload-excel']
    Env_check().dir_check()             # 检查cmdb-file文件目录是否存在
    file.save(app_config['windows_dir'] + secure_filename(file.filename))
    file_path = app_config['windows_dir'] + secure_filename(file.filename)
    User().user_import(excel=file_path,cur='user')
    return redirect(url_for('user'))


@app.route("/user/export", methods=['GET'])
def export_records():
    exc_res = User().user_export()      # 调用api返回生成excel值
    return excel.make_response_from_array(exc_res, "xlsx", file_name="export_user")


@app.route('/layout')
def layout():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(host=app_config['host'], port=app_config['port'], debug=app_config['debug'])


