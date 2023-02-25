#!/usr/bin/python3
from flask import render_template, flash, redirect, url_for
from . import Main 
   
@Main.route('/help')
def help():
    return render_template('help.html') 

