
import json
import pandas as pd


def get_json(name):
    with open(name, 'r') as f:
        data = json.load(f)
    return data


PARAMS = get_json('/home/hugo/music/playman/database/params.json')


def dump_json(name, data):
    with open(name, 'w') as f:
        json.dump(data, f, indent=4)


def get_csv(name):
    return pd.read_csv(name)


def add_array_as_row_in_csv(name, arr):
    df = pd.DataFrame(arr)
    df.to_csv(name, mode='a', header=False, index=False)

dump_path = '/home/hugo/music/playman/database/items.csv'
ITEMS = get_csv(dump_path)

def add_dic_to_items_csv(item):
    if item['title'] not in ITEMS['title'].values:
        new = pd.DataFrame([item])
        ITEMS = pd.concat([ITEMS, new], ignore_index=True)
        ITEMS.to_csv(dump_path, index=False)
        return True
    else:
        return False
