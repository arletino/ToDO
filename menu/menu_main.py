
from data.message import Message, List_messages
from service.json_read_write import read_json, write_json
from service.csv_read_write import read_csv, write_csv
from pathlib import Path
from time import sleep
from menu.menu_filter import Filter_menu

class Main_menu:
    path_json_default = 'new_json.json'
    path_csv_default = 'test.csv'
    main_menu = '''    
        1) Print list messages
        2) Add messages
        3) Change Messages
        4) Delete Messages
        5) Clear list messages
        6) Filter list by date
        7) Read messages form file
        8) Write messages to file 
        9) Change name(path) file
        10) Exit'''
    
    def __init__(self, list_messages, list_messages_filtered) -> None:
        self.list_messages = list_messages
        self.list_messages_filtered = list_messages_filtered
        self.path = self.path_csv_default
        self.menu = {
            '1': self.print_list_notes,
            '2': self.add_message,
            '3': self.change_message,
            '4': self.delete_message,
            '5': self.clear_list,
            '6': self.filter_menu,
            '7': self.read_from_file,
            '8': self.write_to_file,
            '9': self.change_name_file,
        }


    def print_list_notes(self) -> None:
        if (not self.list_messages):
            print('List is empty ')
        else:
            print(self.list_messages)

    def add_message(self) -> None:
        name, body = self.message_menu()
        message = Message(name=name, body=body)
        self.list_messages.append(message)
        print(f'Message add {message}')

    @staticmethod
    def message_menu() -> list[str]:
        name = input('Input name of message: ')
        body = input('Input text message: ')
        return name, body
    
    def change_message(self) -> None:
        print('Input id of message')
        try:
            id = int(input(f'Input number of list messages {len(self.list_messages)}'))
        except TypeError:
            print('Incorrect value')
        else: 
            message = self.list_messages.get_list()[id]
            print(f'Change: {message}')
            name, body = self.message_menu()
            message.set_body(body)
            message.set_name(name)
            print('Message change')

    def delete_message(self) -> None:
        print('Input id of message')
        try:
            id = int(input(f'Input number of list messages {len(self.list_messages)}'))
        except TypeError:
            print('Incorrect value')
        else: 
            self.list_messages.dell_message(id)
            print('Message delete')


    def filter_menu(self):
        f_menu = Filter_menu(self.list_messages, self.list_messages_filtered)
        self.list_messages = f_menu.main_filter_menu()


    def read_from_file(self) -> None:
        if(not self.file_exist(self.path)):
            print('file not exist')
            return
        if (self.choice_format_file(self.path)):
            temp = read_json(self.path)
        else: 
            temp = read_csv(self.path)
        for item in temp:
            message = Message(**item)
            self.list_messages.append(message)
            print(f'Message add {message}')

    @staticmethod
    def choice_format_file(path: str) -> bool:   
        return path.endswith('.json')

    def write_to_file(self) -> None:
        rewrite = False
        if(self.file_exist(self.path)):
            print('File already exist')
            str = input('Add list messages to file or rewrite y(n): ')
            if (str.lower() == 'n'):
                rewrite = True
                print('Information in file will be replaced')
            else:
                print('Information will be add to file')
        if self.choice_format_file(self.path):
            write_json(path=self.path, list_messages=self.list_messages.get_list_dict(), rewrite=rewrite)
        else:
            write_csv(path=self.path, list_messages=self.list_messages.get_list_dict(), rewrite=rewrite)    
        print('Data saved')

    @staticmethod
    def file_exist(path: str) -> bool:
        file = Path(path)
        return file.is_file()

    def change_name_file(self): 
        self.path = input('Input new filename or path: ')

    def exit(self):
        print('Exit')

    def clear_list(self):
        self.list_messages.clear()