import json


def dump_json(name: str, data: str):
    with open(name, 'w') as f:
        json.dump(data, f, indent=4)


def get_json(name: str):
    with open(name, 'r') as f:
        data = json.load(f)
    return data
