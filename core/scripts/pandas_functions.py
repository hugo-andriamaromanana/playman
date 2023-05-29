import pandas as pd
from os import path


def get_csv(name):
    return pd.read_csv(name)


def add_array_as_row_in_csv(name, arr):
    df = pd.DataFrame(arr)
    df.to_csv(name, mode='a', header=False, index=False)


def add_dic_to_items_csv(item, current_user):

    dump_path = path.join(path.dirname(
        __file__), "..", '..', 'users', current_user, 'items.csv')
    
    items = get_csv(dump_path)
    if item['title'] not in list(items['title']):
        new = pd.DataFrame([item])
        items = pd.concat([items, new], ignore_index=True)
        items.to_csv(dump_path, index=False)
        return True
    else:
        return False