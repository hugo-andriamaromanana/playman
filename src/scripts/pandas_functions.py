import pandas as pd
from os import path


def get_csv(name: str):
    return pd.read_csv(name)


def add_dic_to_items_csv(item: dict, current_user: str):

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