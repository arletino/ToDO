from datetime import datetime

class Message:
    '''Класс для создания сообщения'''

    def __init__(self, body="empty message", name='default name') -> None:
        self.__id = 0    
        self.__date_create = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        self.__name = 'new note'
        self.__body = body
    
    def get_dict(self):
        return {'id':self.__id, 'date_create':self.__date_create, 
                'name':self.__name, 'body':self.__body}

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
        return str(self.get_dict())
    
    def __repr__(self) -> str:
        return str(self.get_dict())
    
class List_messages:
    '''Класс для создания списка заметок'''
    def __init__(self) -> None:
        self.__list_messages = []

    def __repr__(self) -> str:
        lst = self.__list_messages
        return str(lst)
        
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
        message =  self.__list_messages[0].get_dict()
        keys = message.keys()
        print(keys)
        len_keys = len(keys)
        temp = dict(zip(keys, ['']*len_keys))
        print(kwargs)
        temp.update(kwargs)
        print(temp)
        return temp
    
    def filter_note(self, **kwargs):
        return self.check_kwargs(**kwargs)
        # if not self.__list_messages:
        #     print('List notes is empty')
        #     return self.__list_messages
        # elif  len(kwargs.keys()) > len(self.__list_messages[0].keys()):
            
        #     print("Input parameters not recognize")
        #     parameters = dict(zip(self.__list_messages[0].keys(), []))
        # else:
        #     print()
    
    

    
             

