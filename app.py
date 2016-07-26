#encoding=utf-8
#

from flask import Flask, redirect, render_template, session, url_for, g, request
import sys
from api import User, VM_assets
from config import app_config
from flask.ext import excel
from pyexcel.ext import xlsx

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
    try:
        User().user_add(sql)
    except Exception as error:
        print '服务器出错,添加用户失败.'
        print error
        return 'error'
    return 'ok'

@app.route('/user/delete', methods=['POST'])
def user_delete():
    userid = request.form.get('id', None)
    sql = 'delete from user where id="%s"' % (userid)
    print 'userid is'+userid
    try:
        User().user_delete(sql)
    except Exception as error:
        print '服务器出错,删除用户失败.'
        print error
        return 'error'
    return 'ok'

@app.route('/user/update', methods=['POST'])
def user_update():
    userid = request.form.get('id', None)
    role = request.form.get('update_role', None)
    password = request.form.get('update_password', None)
    email = request.form.get('update_email', None)
    sql = 'update user set password="%s",role="%s",email="%s" where id="%s"' % (password,role,email,userid)
    print sql
    try:
        User().user_update(sql)
    except Exception as error:
        print '服务器出错,用户信息更新失败.'
        print error
        return 'error'
    return 'ok'

@app.route("/user/import", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        return jsonify({"result": request.get_array(field_name='file')})
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
    <form action="" method=post enctype=multipart/form-data><p>
    <input type=file name=file><input type=submit value=Upload>
    </form>
    '''

@app.route("/user/export", methods=['GET'])
def export_records():
    return excel.make_response_from_array([[1,2,4,5,67,8], [3, 4]], "xlsx", file_name="export_data")



@app.route('/layout')
def layout():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(host=app_config['host'], port=app_config['port'], debug=app_config['debug'])


