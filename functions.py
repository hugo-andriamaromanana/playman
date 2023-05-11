import requests
import json
import pandas as pd
import song


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

# Get all playlists IDS from channel with ID


def get_playlist_ID_arr(ID):
    url = "https://www.googleapis.com/youtube/v3/playlists"
    params = {
        'part': 'snippet',
        'channelId': ID,
        'maxResults': 50,
        'key': PARAMS['key']
    }
    response = requests.get(url, params=params).json()
    arr = []
    for i in range(len(response['items'])):
        arr.append(response['items'][i]['id'])
    while 'nextPageToken' in response.keys():
        params['pageToken'] = response['nextPageToken']
        response = requests.get(url, params=params).json()
        for i in range(len(response['items'])):
            arr.append(response['items'][i]['id'])
    return arr

def 