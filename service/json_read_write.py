import json
from data.message import Message, List_messages
from os import path

def write_json(list_messages: List_messages, path='new_json.json'):
    if list_messages: 
        ident = len(list_messages.get_list_dict()[0].keys())
        
    data = json.dumps(list_messages.get_list_dict(), indent=ident, ensure_ascii = False)
    with open(path, "w", encoding='utf-8') as in_json:
        json.dump(data, in_json, )

def read_json(path='new_json.json'):
    with open(path, encoding='utf-8') as out_json:
        temp = json.load(out_json)
        data = json.loads(temp)
    return data