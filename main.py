from data.message import Message, List_messages
from service.json_read_write import read_json, write_json
from service.csv_read_write import read_csv, write_csv
from time import sleep


def main():
    mess = Message("fghhfd")
    print(mess.__doc__)
    print(mess.__dict__)
    print(mess)
    mess.set_message("sffdgdg")
    print(mess)
    mess2 = Message("rtytuyuiyt")
    # mess2.set_id(1)
    print(mess2)
    lst = List_messages()
    mess3 = Message("sdghnty", "Жкх")
    lst.append(mess)
    lst.append(mess2)
    lst.append(mess3)
    print(lst.get_list())
    write_json(lst)
    data = read_json()
    print(type(data), data)
    print()
    write_csv(lst)
    data1 = read_csv()
    print(data1)
    

if __name__ == "__main__":
    main()