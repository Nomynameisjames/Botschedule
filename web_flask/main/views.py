from flask import Flask, render_template, abort, url_for
from models.Schedule import Create_Schedule
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_mail import Mail
from . import Main
from .. import db
import os


""" 
    old config
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
mail = Mail(app)
app.config['E_MAIL'] = os.environ.get('E_MAIL')
app.config['KEY'] = os.environ.get('KEY')
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Botschedule]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <oadava@gmail.com>'

"""


#@app.route('/daily/<int:my_id>')
#def user(my_id):
 #   file = None
  #  k = {key: value for key, value in dic.items() if key == my_id}
   # if k:
    #    file = k
    
    #else:
     #   abort(404, 'file not found')

    #return render_template('user.html', data=file, current=datetime.utcnow())


@Main.route('/')
def front_page():
    return render_template('landing_page.html')


@Main.route('/missed')
def missed():
    bot = Create_Schedule()
    dic = bot.View('missed')
    return render_template('task_status.html', data=dic)

@Main.route('/daily')
def daily():
    bot = Create_Schedule()
    dic = bot.View('daily')
    return render_template('task_status.html', data=dic)

@Main.route('/View')
def view():
    bot = Create_Schedule()
    doc = bot.View()
    return render_template('index.html', data=doc)

@Main.route('/upcoming')
def upcoming():
    bot = Create_Schedule()
    dic = bot.View('upcoming')
    return render_template('task_status.html', data=dic)

@Main.route('/new')
def new():
    return render_template('table.html')

