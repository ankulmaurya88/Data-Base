from app.model import fun_1, fun_2, fun_3, fun_4
from flask import Flask, jsonify, request

def get_user():
    res = fun_1()
    data = list()
    for row in res:
        user = dict()
        user['id'] = row[0]
        user['roll_no'] = row[1]
        user['name'] = row[2]
        user['course'] = row[3]
        data.append(user)    
    return jsonify(data)


def save_user():
    data = request.get_json()
    print(data)
    if not data:
        return jsonify({"error": "No data provided"}), 400
    id = data.get('id')
    roll_no = data.get('roll_no')
    name = data.get('name')
    course = data.get('course')
    res = fun_2(id, roll_no, name, course)
    return jsonify({"success": "Data saved successfully"})

def update_user():
    return "I am update-user function"

def delete_user():
    return "I am delete-user function"