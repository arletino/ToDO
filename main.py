from menu.menu_main import Main_menu
from data.message import List_messages
from time import sleep  

def main():
    list_messages_filtered = List_messages()
    list_messages = List_messages()
    main_menu = Main_menu(list_messages, list_messages_filtered)
    print(intro_s)
    quit = str(len(main_menu.menu) + 1)
    while True:
        print(f'Default path file = {main_menu.path}, Numbers notes in list= {len(main_menu.list_messages)}: ')
        print(main_menu.main_menu)
        action  = input('Input number action: ')
        if action == quit:
            break 
        if action in main_menu.menu.keys():
            main_menu.menu[action]()
        else:
            print('Wrong input')
        sleep(0.3)


if __name__ == "__main__":
    intro_s = 'Программа для работы с заметками'
    main()
    