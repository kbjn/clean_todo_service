from typing import Dict, List
from main.domain.model.todo import ToDo

class ToDoCollection:
    __collection : Dict[str, ToDo] = {}

    def __init__(self):
        pass

    def add(self, todo: ToDo):
        self.__collection[todo.id] = todo
        return todo

    def get_list(self) -> List[ToDo]:
        if not bool(self._ToDoCollection__collection):
            return []
        return self.__collection.values()

    def get(self, todo_id: str) -> ToDo:
        return self.__collection[todo_id]

    def delete(self, todo_id: str):
        del self.__collection[todo_id]

    def update(self, todo_id: str, desc: str) -> ToDo:
        todo = self.__collection[todo_id]
        todo.desc = desc
        self.__collection[todo_id] = todo
        return todo