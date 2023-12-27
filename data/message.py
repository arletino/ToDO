from datetime import datetime

class Message:
    '''Класс для создания и обработки сообщения'''

    def __init__(self, id=0, date_create='', body="empty message", name='default name') -> None:
        self.__id = id if (id != '' or id is not str) else 0   
        date_create = self.parse_data(date_create)
        if (date_create == ''):
            self.__date_create = datetime.now().strftime("%d/%m/%y %H:%M:%S")  
        else:  
            self.__date_create = datetime.strftime(date_create, "%d/%m/%y %H:%M:%S")
        self.__name = name if name != '' else 'default name'
        self.__body = body if body != '' else "empty message" 
    
    def parse_data(self, date_create) -> str:
        try:
            data_temp = datetime.strptime(date_create, "%d/%m/%y %H:%M:%S")
        except:
            return ''
        return data_temp
    
    def get_dict(self):
        return {'id':self.__id, 'date_create':self.__date_create, 
                'name':self.__name, 'body':self.__body}
    
    def get_date_create(self):
        return datetime.strptime(self.__date_create, "%d/%m/%y %H:%M:%S")
    
    def get_date_create_dict(self) -> dict:
        temp_date = datetime.strptime(self.__date_create, "%d/%m/%y %H:%M:%S")
        return  {
            'Year': temp_date.year,
            'Month': temp_date.month,
            'Day': temp_date.day,
            'Hour': temp_date.hour,
            'Minutes': temp_date.minute,
            'Second': temp_date.second
        }
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id: int):
        if (id != ''):
            self.__id = id
    
    def set_name(self, name: str):
        if (name != ''):
            self.__name = name
            self.__date_create = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    
    def get_name(self):
        return self.__name
    
    def set_body(self, body):
        if (body != ''):
            self.__body = body
            self.__date_create = datetime.now().strftime("%d/%m/%y %H:%M:%S")

    def __str__(self):
        return f'id: {self.__id} Data: {self.__date_create} Name: {self.__name} Text: {self.__body}'
    
    def __repr__(self):
        return f'id: {self.__id} Data: {self.__date_create} Name: {self.__name} Text: {self.__body}'
    
class List_messages:
    '''Класс для создания списка заметок'''
    def __init__(self) -> None:
        self.__list_messages = []

    def __str__(self) -> str:
        if (self.__list_messages):
            temp  = ""
            for message in self.__list_messages:
                temp += f'{message} \n'
        else: temp = f'{self.__list_messages}'
        return temp
    
    def __len__(self):
        return len(self.__list_messages)
        
    def __iter__(self):
        return iter(self.__list_messages)

    def append(self, message: Message):
        self.__list_messages.append(message)
        self.__list_messages.sort(key=lambda x: x.get_date_create())
        for  id, message in enumerate(self.__list_messages):
            message.set_id(id)

    
    def get_list(self):
        return self.__list_messages
    
    def get_list_dict(self):
        return [message.get_dict() for message in self.__list_messages]
    
    
    def clear(self):
        return self.__list_messages.clear()
    
    @classmethod
    def refresh_id(cls) -> None:
       for id, message in enumerate(cls.__list_messages):
            message.set_id(id) 

    def dell_message(self, id: int):
        self.__list_messages.pop(id)
        self.refresh_id()

