#encoding=utf-8
#

from flask import Flask, redirect, render_template, session, url_for, g, request
import sys,os
from api import Action, split_path
from pub import Env_check,Handle_excel
from config import app_config
from flask.ext import excel
from pyexcel.ext import xlsx
from werkzeug import secure_filename

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():    
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    user_info = Action().auth_info()
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user in user_info:
            if pwd == user_info[user]:
                session['user'] = user
                return redirect(url_for('user'))
            else:
                return '密码错误,请重新登录'
        else:
            return '用户不存在'

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/vmassets')
def vmassets():
    sql = 'select * from vmassets'
    res = Action().get_data(sql)
    if 'user' in session:
        return render_template('vmassets.html',vmassets_info=res)
    else:
        return redirect(url_for('login'))

@app.route('/user')
def user():
    sql = 'select id,username,password,role,email from user'
    res = Action().get_data(sql)
    if 'user' in session:
        return render_template('user.html',user_info=res)
    else:
        return redirect(url_for('login'))

@app.route('/vmassets/add', methods=['POST'])
def vmassets_add():
    ip_addr = request.form.get('ip_addr',None)
    if ip_addr:
        app_name = request.form.get('app_name',None)
        hostname = request.form.get('hostname',None)
        vc_name = request.form.get('vc_name',None)
        cpu = request.form.get('cpu',None)
        memory = request.form.get('memory',None)
        disk = request.form.get('disk',None)
        os = request.form.get('os',None)
        status = request.form.get('status',None)
        office_name = request.form.get('office_name',None)
        office_contact = request.form.get('office_contact',None)
        office_phone = request.form.get('office_phone',None)
        object_contact = request.form.get('object_contact',None)
        object_phone = request.form.get('object_phone',None)
        create_date = request.form.get('create_date',None)
        end_date = request.form.get('end_date',None)
        notes = request.form.get('notes',None)
        sql = 'insert into vmassets (ip_addr,app_name,hostname,vc_name,cpu,memory,disk,os,status,office_name,office_contact,office_phone,object_contact,object_phone,create_date,end_date,notes) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (ip_addr,app_name,hostname,vc_name,cpu,memory,disk,os,status,office_name,office_contact,office_phone,object_contact,object_phone,create_date,end_date,notes)
    else:
        return 'error'
    Action().sql_operation(sql=sql,status=split_path(request.path))
    return 'ok'

@app.route('/user/add', methods=['POST'])
def user_add():
    username = request.form.get('username', None)
    # 验证用户名是否为空,如果为空,添加失败.
    if username:
        password = request.form.get('password', None)
        role = request.form.get('role', None)
        email = request.form.get('email', None)
        sql = 'insert into user (username,password,role,email) values ("%s","%s","%s","%s")' % (username,password,role,email)
    else:
        return 'error'
    Action().sql_operation(sql=sql,status=split_path(request.path))
    return 'ok'

@app.route('/vmassets/delete', methods=['POST'])
def vmassets_delete():
    userid = request.form.get('userid', None)
    sql = 'delete from vmassets where id="%s"' % (userid)
    if Action().sql_operation(sql=sql,status=split_path(request.path)):
        return 'ok'
    else:
        return 'error'

@app.route('/user/delete', methods=['POST'])
def user_delete():
    userid = request.form.get('id', None)
    sql = 'delete from user where id="%s"' % (userid)
    if Action().sql_operation(sql=sql,status=split_path(request.path)):
        return 'ok'
    else:
        return 'error'


@app.route('/vmassets/update', methods=['POST'])
def vmassets_update():
    id = request.form.get('id', None)
    update_ip_addr = request.form.get('update_ip_addr',None)
    update_app_name = request.form.get('update_app_name',None)
    update_hostname = request.form.get('update_hostname',None)
    update_vc_name = request.form.get('update_vc_name',None)
    update_cpu = request.form.get('update_cpu',None)
    update_memory = request.form.get('update_memory',None)
    update_disk = request.form.get('update_disk',None)
    update_os = request.form.get('update_os',None)
    update_status = request.form.get('update_status',None)
    update_office_name = request.form.get('update_office_name',None)
    update_office_contact = request.form.get('update_office_contact',None)
    update_office_phone = request.form.get('update_office_phone',None)
    update_object_contact = request.form.get('update_object_contact',None)
    update_object_phone = request.form.get('update_object_phone',None)
    update_create_date = request.form.get('update_create_date',None)
    update_end_date = request.form.get('update_end_date',None)
    update_notes = request.form.get('update_notes',None)
    sql = 'update vmassets set ip_addr="%s",app_name="%s",hostname="%s",vc_name="%s",cpu="%s",memory="%s", disk="%s", os="%s", status="%s", office_name="%s", office_contact="%s", office_phone="%s", object_contact="%s", object_phone="%s", create_date="%s", end_date="%s", notes="%s" where id=%s' % (update_ip_addr, update_app_name, update_hostname, update_vc_name, update_cpu, update_memory, update_disk, update_os, update_status, update_office_name, update_office_contact, update_office_phone, update_object_contact, update_object_phone, update_create_date, update_end_date, update_notes, id)

    try:
        Action().sql_operation(sql=sql,status=split_path(request.path))
    except Exception as error:
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

    if Action().sql_operation(sql=sql,status=split_path(request.path)):
        return 'ok'
    else:
        return 'error'

@app.route("/vmassets/import", methods=['GET', 'POST'])
def vmassets_upload_file():
    file = request.files['upload-excel']
    Env_check().dir_check()                 # 检查cmdb-file文件目录是否存在
    file.save(app_config['windows_dir'] + secure_filename(file.filename))
    file_path = app_config['windows_dir'] + secure_filename(file.filename)
    Action().data_import(excel=file_path,cur='vmassets')
    return redirect(url_for('vmassets'))

@app.route("/user/import", methods=['GET', 'POST'])
def user_upload_file():
    file = request.files['upload-excel']
    Env_check().dir_check()                 # 检查cmdb-file文件目录是否存在
    file.save(app_config['windows_dir'] + secure_filename(file.filename))
    file_path = app_config['windows_dir'] + secure_filename(file.filename)
    Action().data_import(excel=file_path,cur='user')
    return redirect(url_for('user'))

@app.route("/vmassets/export", methods=['GET'])
def vmassets_export():
    exc_res = Action().data_export(cur='vmassets')      # 调用api返回生成excel值
    return excel.make_response_from_array(exc_res, "xlsx", file_name="export_vmassets")


@app.route("/user/export", methods=['GET'])
def user_export():
    exc_res = Action().data_export(cur='user')      # 调用api返回生成excel值
    return excel.make_response_from_array(exc_res, "xlsx", file_name="export_user")

@app.route('/layout')
def layout():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(host=app_config['host'], port=app_config['port'], debug=app_config['debug'])


