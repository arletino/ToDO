from time import sleep
from data.message import List_messages
from service.filter_date import Filter_dates

class Filter_menu:

    def __init__(self, list_messages: List_messages | None, list_messages_filtered: List_messages | None) -> None:
        if list_messages is None:
            self.list_messages = []    
        else:
            self.list_messages = list_messages
        
        self.filter_dates = Filter_dates(None)
        self.list_messages_filtered = list_messages_filtered
        
        self.menu_filter_str =[
                '1) Sort by date',
                '2) Sort from date',
                '3) Sort before date',
                '4) Sort between dates',
                '5) Print filtered list',
                '6) Move filtered list to main',
                '7) Clear filtered list',
                '8) Back main menu',
            ]
        
        self.menu_filter = {
            '1': self.filter_by_date,
            '2': self.filter_up_date,
            '3': self.filter_low_date,
            '4': self.filter_between_date,
            '5': self.print_filter_list,
            '6': self.move_filtered_list,
            '7': self.clear_filter_list,
        }  
       
    def filter_by_date(self) -> None:
        if not self.list_messages:
            print('List is empty')
            return
        self.filter_dates.set_date_filter_lower()
        for message in self.list_messages:
            self.filter_dates.set_messages(message)    
            if self.filter_dates.filter_by_date():
                self.list_messages_filtered.append(message)
       
    def filter_up_date(self):
        if not self.list_messages:
            print('List is empty')
            return
        print('Input lower border')
        self.filter_dates.set_date_filter_lower()
        for message in self.list_messages:
            self.filter_dates.set_messages(message)    
            if self.filter_dates.filter_up_date():
                self.list_messages_filtered.append(message)
    
    def filter_low_date(self):
        if not self.list_messages:
            print('List is empty')
            return
        print('Input upper border')
        self.filter_dates.set_date_filter_upper()
        for message in self.list_messages:
            self.filter_dates.set_messages(message)    
            if self.filter_dates.filter_low_date():
                self.list_messages_filtered.append(message)

    def filter_between_date(self):
        if not self.list_messages:
            print('List is empty')
            return
        print('Input lower border')
        self.filter_dates.set_date_filter_lower()
        print('Input upper border')
        self.filter_dates.set_date_filter_upper()
        for message in self.list_messages:
            self.filter_dates.set_messages(message)    
            if self.filter_dates.filter_between_date():
                self.list_messages_filtered.append(message)
        
    def print_filter_list(self) -> None:
        if (not self.list_messages_filtered):
            print('List is empty ')
        else:
            print(self.list_messages_filtered)    

    def clear_filter_list(self) ->None:
        self.list_messages_filtered.clear()
    
    def move_filtered_list(self):
        print('Main list replaced by filtered')
        self.list_messages = self.list_messages_filtered
        return self

    def main_filter_menu(self) -> List_messages:
            action =''
            quit = str(len(self.menu_filter.keys()) + 1)
            while action != quit:
                print(f'Lower filter border or equal {self.filter_dates.date_filter_lower}')
                print(f'Upper filter border {self.filter_dates.date_filter_upper}')
                print(f'Numbers notes in filter list= {len(self.list_messages_filtered)}')
                for item in self.menu_filter_str:
                    print(item)
                action  = input('Input number action: ')
                if action == quit:
                    break
                elif action in self.menu_filter.keys():
                    self.menu_filter[action]()
                else:
                    print('Wrong input')
                sleep(0.3)
            return self.list_messages

    

    