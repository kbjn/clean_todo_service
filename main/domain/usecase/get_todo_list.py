from typing import List
from main.domain.model.todo import ToDo
from main.domain.repository.todo_collection import ToDoCollection

class GetToDoList:
    def __init__(self):
        self.__repos = ToDoCollection()

    def execute(self) -> List[ToDo]:
        return self.__repos.get_list()