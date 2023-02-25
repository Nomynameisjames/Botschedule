#!/usr/bin/python3
from api.v1.main import main_app
from flask import abort, jsonify, request
from models.Schedule import Create_Schedule as cs
from models import storage
from datetime import datetime

bot = cs()
data = bot.View()


@main_app.route('/tasks', methods=['GET', 'POST'])
def task():
    if request.method == 'GET':
        doc = storage.view()
        data = [obj.to_json() for obj in doc.values()]
        return jsonify(data), 200

    if request.method == 'POST':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        if req_json.get("Day") is None:
            abort(400, 'Missing Date')
        if req_json.get("Course") is None:
            abort(400, 'Missing Course')
        if req_json.get("Topic") is None:
            abort(400, 'Missing Topic')
        if req_json.get("Reminder") is None:
            abort(400, 'please set reminder')
        bot.Create(**req_json)
        bot.Save()
        return jsonify(bot.View()), 201

@main_app.route('/tasks/<int:my_id>', methods=['GET', 'PUT', 'DELETE'])
def get_task(my_id):
    doc = storage.view()
    if request.method == 'GET':
        data = [obj.to_json() for obj in doc.values()
                if obj.id == my_id]
        if data is None:
            abort(404, 'ID not in list')
        return jsonify(data)

    if request.method == 'PUT':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not JSON')
        IGNORE = [
                 'Target', 'Days', 'Created_at' ]
        if req_json:
            updated_dict = {
                     k: v for k, v in req_json.items() if k not in IGNORE
                 }
            for key, value in updated_dict.items():
                if key == 'Topic':
                    doc[my_id].Topic = value
                elif key == 'Course':
                    doc[my_id].Course = value
                elif key == 'Reminder':
                    doc[my_id].Reminder = value
                else:
                    abort(400,  "key not found")
                doc[my_id].Updated_at = datetime.now()
                storage.save()
                return jsonify(updated_dict), 200

    if request.method == 'DELETE':
        obj = doc.get(my_id)
        if obj is None:
            abort(404, 'ID not in list')
        storage.delete(obj)
        del obj
        storage.save()
        return jsonify({"Success" : "data removed"}), 200

