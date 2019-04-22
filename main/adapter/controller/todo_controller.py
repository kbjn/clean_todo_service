from flask import Blueprint, request, jsonify
from main.domain.usecase.get_todo_list import GetToDoList
from main.domain.usecase.create_todo import CreateToDo
from main.domain.usecase.get_todo import GetToDo
from main.domain.usecase.delete_todo import DeleteToDo
from main.domain.usecase.update_todo import UpdateToDo
from main.domain.model.todo import ToDo

app = Blueprint('todo', __name__)

@app.route("/todo", methods=["GET"])
def get_todo_list():
    usecase = GetToDoList()
    todo_list = usecase.execute()
    json_todo_list = []
    for todo in todo_list:
        json_todo_list.append(todo.to_json())
    response = jsonify(json_todo_list)
    return response

@app.route("/todo/<todo_id>", methods=["GET"])
def get_todo(todo_id: str):
    usecase = GetToDo()
    todo = usecase.execute(todo_id)
    response = jsonify(todo.to_json())
    return response

@app.route("/todo", methods=["POST"])
def create_todo():
    json = request.get_json()
    desc = json['desc']
    usecase = CreateToDo()
    todo = usecase.execute(desc)
    response = jsonify(todo.to_json())
    return response

@app.route("/todo/<todo_id>", methods=["DELETE"])
def delete_todo(todo_id: str):
    usecase = DeleteToDo()
    usecase.execute(todo_id)
    return ""

@app.route("/todo/<todo_id>", methods=["PUT"])
def update_todo(todo_id):
    json = request.get_json()
    desc = json['desc']
    usecase = UpdateToDo()
    todo = usecase.execute(todo_id, desc)
    response = jsonify(todo.to_json())
    return response

