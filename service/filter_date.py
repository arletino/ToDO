from data.message import Message

class Filter_dates:

    def __init__(self, message: Message | None ) -> None:
        if message is None:
            self.date_compare = {}
        else:
            self.date_compare = message.get_date_create_dict()
        self.date_filter_lower = {
            'Year': '',
            'Month': '',
            'Day': '',
            'Hour': '',
            'Minutes': '',
            'Second': ''
        }
        self.date_filter_upper = {
            'Year': '',
            'Month': '',
            'Day': '',
            'Hour': '',
            'Minutes': '',
            'Second': ''
        }

    def set_messages(self, message: Message) -> None:
        self.date_compare = message.get_date_create_dict()

    def set_date_filter_lower(self) -> None:
        for item in self.date_filter_lower:
            temp = input(f'{item} = ')
            self.date_filter_lower[item] = int(temp) if temp != '' else ''
    
    def set_date_filter_upper(self) -> None:
        for item in self.date_filter_upper:
            temp = input(f'{item} = ')
            self.date_filter_upper[item] = int(temp) if temp != '' else ''
    
    def filter_by_date(self) -> bool:
        for item in self.date_filter_lower:
            if(self.date_filter_lower[item] != '' and self.date_filter_lower[item] != self.date_compare[item]):
                return False
        return True 

    def filter_up_date(self) -> bool:
        for item in self.date_filter_lower:
            print(type(self.date_filter_lower[item]), type(self.date_compare[item]))
            print(self.date_filter_lower[item], self.date_compare[item], self.date_filter_lower[item] != '' and self.date_filter_lower[item] > int(self.date_compare[item]))
            if (self.date_filter_lower[item] != '' and self.date_filter_lower[item] >= int(self.date_compare[item])):
                return False
        return True

    def filter_low_date(self) -> bool:
        for item in self.date_filter_upper:
            if (self.date_filter_upper[item] != '' and self.date_filter_upper[item] <= int(self.date_compare[item])):
                return False
        return True

    def filter_between_date(self) -> bool:
        return self.filter_low_date() and self.filter_up_date()
    
    
    

