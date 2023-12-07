from data.message import Message
from time import sleep


def main():
    mess = Message("fghhfd")
    print(mess.__doc__)
    print(mess.__dict__)
    print(mess)
    sleep(3)
    mess.set_message("sffdgdg")
    print(mess)
    mess2 = Message("rtytuyuiyt")
    print(mess2)
    print()
    lst = []
    lst.append(mess)
    lst.append(mess2)
    for el in lst:
        print(el)

if __name__ == "__main__":
    main()