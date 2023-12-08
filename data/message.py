from datetime import datetime

class Message:
    '''Класс для создания сообщения'''
    __new_mess = None 

    def __init__(self, body: str, name = '') -> None:
        self.__id = 0    
        self.__date_create = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        self.__name = 'new note'
        if name == '':
            self.__name = f'{self.__name} {self.__new_mess}'
        else:
            self.__name = name
        self.__body = body
    

    def __new__(cls, *args, **kwargs):
        if cls.__new_mess is not None and cls.__name == 'new note':
            cls.__new_mess += 1
        else:
            cls.__new_mess = 0
        return super().__new__(cls)
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_message(self, message):
        self.__body = message
        self.__date_create = datetime.now().strftime("%d/%m/%y %H:%M:%S")

    def __str__(self) -> str:
        return str(self.__dict__)
    
    def __repr__(self) -> str:
        return str(self.__dict__)
    
class List_messages:
    '''Класс для создания списка заметок'''
    def __init__(self) -> None:
        self.__list_messages = []

    def __repr__(self) -> str:
        return self.__list_messages
        
    def append(self, message: Message):
        if not self.__list_messages:
            self.__list_messages.append(message)
        else:
            message.set_id(len(self.__list_messages))
            self.__list_messages.append(message)
    
    def get_list(self):
        return self.__list_messages
    
    def check_kwargs(self, **kwargs):
        if not kwargs:
            return False
        keys = self.__list_messages[0].keys()
        len_keys = len(keys)
        temp = dict(zip(self.__list_messages[0].keys(), ['']*len_keys))
        return temp
    
    def filter_note(self, **kwargs):
        print(List_messages.check_kwargs(kwargs))
        # if not self.__list_messages:
        #     print('List notes is empty')
        #     return self.__list_messages
        # elif  len(kwargs.keys()) > len(self.__list_messages[0].keys()):
            
        #     print("Input parameters not recognize")
        #     parameters = dict(zip(self.__list_messages[0].keys(), []))
        # else:
        #     print()
    
    

    
             

