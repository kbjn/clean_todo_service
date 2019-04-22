from uuid import uuid4

class ToDo:

    def __init__(self, desc: str):
        self.id = str(uuid4())
        self.desc = desc

    def to_json(self):  
        return {           
            'id': self.id, 
            'desc': self.desc
        }