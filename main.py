from data.message import Message, List_messages
from time import sleep


def main():
    mess = Message("fghhfd")
    print(mess.__doc__)
    print(mess.__dict__)
    print(mess)
    mess.set_message("sffdgdg")
    print(mess)
    mess2 = Message("rtytuyuiyt")
<<<<<<< HEAD
    print(mess2)
    print()
    lst = []
    lst.append(mess)
    lst.append(mess2)
    for el in lst:
        print(el)
=======
    # mess2.set_id(1)
    print(mess2)
    lst = List_messages()
    mess3 = Message("sdghnty", "Жкх")
    lst.append(mess)
    lst.append(mess2)
    lst.append(mess3)
    print(lst.getList())
>>>>>>> main

if __name__ == "__main__":
    main()