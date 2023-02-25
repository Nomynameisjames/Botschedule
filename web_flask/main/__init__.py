from flask import Blueprint

Main = Blueprint('Main', __name__) 

from . import views, errors, auth, Help
