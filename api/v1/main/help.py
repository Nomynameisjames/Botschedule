#!/usr/bin/python3
from api.v1.main import main_app
from flask import abort, jsonify, request
from models.Schedule import Create_Schedule as cs
from models import storage
from models.checker import Checker


@main_app.route('/help', methods=['GET', 'POST'])
def help():
    message = {}
    bot = Checker()
    req_data = request.get_json()
    if request.method == 'POST':
        for text in req_data.values():
            data = bot.Help(text)
            message[text] = data
            return jsonify(message)
    else:
        abort(404, 'invalid request')
