#!/usr/bin/env python3
from flask import Flask,redirect,request,render_template,g,session,abort
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('database.db')

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.errorhandler(404)
def not_found(e):
    return 'Status : 404'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login_page():
    user = request.form.get('username')
    password = request.args.get('password')
    if user == '':
        return redirect('/admin')
@app.route('/admin')
@app.route('/admin/')
def admin_page():
    return render_tempate('admin.html')

@app.route('/api/<cmd>'):
def api_cmd(cmd):
    commands = {
    'uname':'uname',
    'id':'id'
    'pwd':'pwd'
            }
    if session.get('admin'):
        try:
            c = cmd(commands[cmd])
            return c
        except:
            return abort(404)
    return redirect('/')

app.run()
