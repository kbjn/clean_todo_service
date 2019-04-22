from main.domain.model.todo import ToDo
from main.domain.repository.todo_collection import ToDoCollection

class DeleteToDo:
    def __init__(self):
        self.__repos = ToDoCollection()

    def execute(self, todo_id: str):
        self.__repos.delete(todo_id)
        pass