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
    This file contains all the routes for the application
    this enables user to query the database to view Schedules
    based on the status of the task
"""


@Main.route('/')
def front_page():
    return render_template('landing_page.html')

@Main.route('/about')
def about():
    return render_template('about.html')


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

@Main.route('/Access')
def Access():
    # bot = Create_Schedule()
    # dic = bot.View('login')
    return render_template('login.html')

@Main.route('/reg')
def reg():
    # bot = Create_Schedule()
    # dic = bot.View('login')
    return render_template('register.html')


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

@Main.route('/reset')
def reset():
    return render_template('forget.html')
