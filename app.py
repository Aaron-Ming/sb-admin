#encoding=utf-8


from flask import Flask, redirect, render_template, session, url_for, g
import sys
from api import User, VM_assets

# sql = 'insert into vm_assets(ip_addr,app_name,hostname,vc_name,cpu,memory,disk,os,status,office_name,office_contact,office_phone,object_contact,object_phone,create_date,end_date,notes) values("11","xx","cc","ww","qq","ww","ee","rr","tt","yy","qq","ww","rr","yy","tt","rr","bb")'
# test = VM_assets()

# test.vmassets_add(sql)


reload(sys)
sys.setdefaultencoding('utf-8')


app = Flask(__name__)


@app.route('/vm_assets')
def vm_assets():
	
	return render_template('vm_assets.html')

@app.route('/user')
def user():
	sql = 'select username,password,role,email from user'
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




@app.route('/layout')
def layout():
	return render_template('layout.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)


