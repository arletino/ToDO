import csv


def write_csv(list_messages: dict, path='new_csv.csv', rewrite=False):
    r_w = 'w' if rewrite else 'a'
    path = 'new_csv.csv' if path == '' else path 
    data = list_messages
    with open(path, 'w', newline='', encoding='utf-8') as file:
        columns = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=";")
        writer.writeheader()
        writer.writerows(data)

def read_csv(path='new_csv.csv'):
    if (path == ''): path = 'new_csv.csv'
    with open(path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=";",)
        lst_temp = []
        for row in reader:
            lst_temp.append(row)
    return lst_temp


