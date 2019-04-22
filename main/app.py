from flask import Flask
from main.adapter.controller import todo_controller
from main.domain.model.todo import ToDo
import json

app = Flask(__name__)

app.register_blueprint(todo_controller.app)

if __name__ == '__main__':
    app.run(50000)