from datetime import datetime

class Message:
    '''Класс для создания сообщения'''
    new_mess = None
    __id = 0

    def __init__(self, message: str, name = 'default') -> None:
        self.date_create = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        if name == 'default':
            self.name = f'{name} {self.new_mess}'
        else:
            self.name = name
        self.message = message

    def __new__(cls, *args, **kwargs):
        if cls.new_mess is not None and cls.name == 'default':
            cls.new_mess += 1
        else:
            cls.new_mess = 0
        return super().__new__(cls)
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
    
    def name(self, name):
        self.name = f'{name} {self.__id}'
    
    def set_message(self, message):
        self.message = message
        self.date_create = datetime.now().strftime("%d/%m/%y %H:%M:%S")

    def __str__(self):
        return f'{self.__id} {self.date_create} {self.name} \n {self.message}'
    
    def __repr__(self) -> str:
        return f'{self.__id} {self.date_create} {self.name} {self.message}'
    
class List_messages:
    '''Класс для создания списка заметок'''
    def __init__(self) -> None:
        self.__list_messages = []
        
    def append(self, message: Message):
        if not self.__list_messages:
            self.__list_messages.append(message)
        else:
            message.set_id(len(self.__list_messages))
            self.__list_messages.append(message)
    
    def getList(self):
        return self.__list_messages

