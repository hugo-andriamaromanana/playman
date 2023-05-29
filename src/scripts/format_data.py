from os import path
from src.scripts.json_functions import get_json


def clean_title(title: str):

    trash = get_json(path.join(path.dirtitle(__file__),
                     '..', '..', 'settings', 'trash.json'))
    for i in trash:
        if title.find(i) != -1:
            title = title.replace(i, '')
            return title.replace('()', '')
    return title


def format_time(time: str):

    if time[0] == 'P':
        time = time[1:]
    if time[0] == 'T':
        time = time[1:]
    if time.find('H') != -1:
        hours = int(time[:time.find('H')])
        time = time[time.find('H') + 1:]
    else:
        hours = 0
    if time.find('M') != -1:
        minutes = int(time[:time.find('M')])
        time = time[time.find('M') + 1:]
    else:
        minutes = 0
    if time.find('S') != -1:
        seconds = int(time[:time.find('S')])
    else:
        seconds = 0
    return hours * 3600 + minutes * 60 + seconds


def format_date(date: str):

    return date[:date.find('T')]


def string_to_arr(string: str) -> list:

    string = str(string)
    string = string.replace('[', '')
    string = string.replace(']', '')
    string = string.replace('\'', '')
    string = string.replace(' ', '')
    string = string.replace(',', ' ')
    return string.split(' ')


def remove_tags(tags: list):
    
    for i in range(len(tags)):
        if tags[i].find('https://en.wikipedia.org/wiki/') != -1:
            tags[i] = tags[i][30:]
    if 'Music' in arr:
        tags.remove('Music')
    return tags
