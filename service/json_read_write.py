import json
from os import path
from pathlib import Path


def write_json(list_messages: dict, path='new_json.json', rewrite=False):
    r_w = 'w' if rewrite else 'a'
    if (path == ''): path = 'new_json.json'
    if list_messages:
        ident = len(list_messages[0].keys())    
    data = json.dumps(list_messages, indent=ident, ensure_ascii = False)
    with open(path, r_w, encoding='utf-8') as in_json:
        json.dump(data, in_json, )

def read_json(path='new_json.json'):
    if (path == ''): path = 'new_json.json'
    with open(path, encoding='utf-8') as out_json:
        try:
            temp = json.load(out_json)
            data = json.loads(temp)
        except:
            print('Wrong format file')
    return data

