from main.domain.model.todo import ToDo
from main.domain.repository.todo_collection import ToDoCollection

class GetToDo:
    def __init__(self):
        self.__repos = ToDoCollection()

    def execute(self, todo_id: str) -> ToDo:
        return self.__repos.get(todo_id)