#encoding=utf-8


from flask import Flask, redirect, render_template, session, url_for, g
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


app = Flask(__name__)


@app.route('/tab')
def tab():
	return render_template('tab.html')

@app.route('/user')
def user():
	return render_template('user.html')

@app.route('/layout')
def layout():
	return render_template('layout.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)