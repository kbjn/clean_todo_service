from main.domain.model.todo import ToDo
from main.domain.repository.todo_collection import ToDoCollection

class CreateToDo:
    def __init__(self):
        self.__repos = ToDoCollection()

    def execute(self, desc: str) -> ToDo:
        todo = ToDo(desc)
        self.__repos.add(todo)
        return todo