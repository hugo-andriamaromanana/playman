
import json
import pandas as pd

def get_json(name):
    with open(name, 'r') as f:
        data = json.load(f)
    return data


PARAMS = get_json('database/params.json')


def dump_json(name, data):
    with open(name, 'w') as f:
        json.dump(data, f, indent=4)


def get_csv(name):
    return pd.read_csv(name)


def add_array_as_row_in_csv(name, arr):
    df = pd.DataFrame(arr)
    df.to_csv(name, mode='a', header=False, index=False)


def add_dic_to_items_csv(item):
    items = get_csv('database/items.csv')
    if item['title'] not in items['title'].values:
        items = items.append(item, ignore_index=True)
        items.to_csv('database/items.csv', index=False)
        print('[SUCCESS]: Song added to database')
    else: 
        print('[SKIP]: Song already in database')

def clean(name):
    trash = get_json('database/trash.json')
    for i in trash:
        if name.find(i) != -1:
            name=name.replace(i, '')
            return name.replace('()','')
    return name