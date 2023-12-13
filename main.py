from data.message import Message, List_messages
from service.json_read_write import read_json, write_json
from service.csv_read_write import read_csv, write_csv
from time import sleep


def main():
    mess = Message("fghhfd",)

    print(mess)
    mess2 = Message("sdgdfgf")
    print(mess2)
    mess.set_message("sffdgdg")
    print(mess)
    lst = List_messages()
    mess3 = Message("sdghnty", "Жкх")
    lst.append(mess)
    lst.append(mess2)
    lst.append(mess3)
    print(type(lst))
    print(lst.filter_note(id=1, date_create='10.20.23'))
    #write_json(lst)
    # data = read_json()
    # print(type(data), data)
    # print()
    # write_csv(lst)
    # data1 = read_csv()
    # print(data1)
    

if __name__ == "__main__":
    main()