import csv
from data.message import Message, List_messages

def write_csv(list_messages:List_messages, path='new_csv.csv'):
    data = list_messages.get_list_dict()
    with open(path, 'w', newline='', encoding='utf-8') as file:
        columns = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=";")
        writer.writeheader()
        writer.writerows(data)

def read_csv(path='new_csv.csv', encoding='utf-8'):
    with open(path, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=";",)
        lst_temp = []
        for row in reader:
            lst_temp.append(row)
    return lst_temp