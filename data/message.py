from datetime import datetime
class Message:
    '''Класс для создания сообщения'''
    def __init__(self, message: str, name = "new note", id = 0) -> None:
        self.id = id
        self.date_create = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        self.date_change = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        self.name = f'{name} {id}' 
        self.message = message
    
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
    
    def set_message(self, message):
        self.message = message
        self.date_change = datetime.now().strftime("%d/%m/%y %H:%M:%S")

    def __str__(self):
        return f'{self.id} {self.date_create} {self.name} \n {self.message}'