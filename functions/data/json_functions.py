import json


def dump_json(name, data):
    with open(name, 'w') as f:
        json.dump(data, f, indent=4)


def get_json(name):
    with open(name, 'r') as f:
        data = json.load(f)
    return data
