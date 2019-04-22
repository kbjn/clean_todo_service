from main.domain.model.todo import ToDo
from main.domain.repository.todo_collection import ToDoCollection

class UpdateToDo:
    def __init__(self):
        self.__repos = ToDoCollection()

    def execute(self, todo_id:str, desc: str) -> ToDo:
        return self.__repos.update(todo_id, desc)
