import os
from functions.data.json_functions import get_json


def clean_title(name):

    trash = get_json(os.path.join(os.path.dirname(__file__),
                     '..', '..', 'settings', 'trash.json'))
    for i in trash:
        if name.find(i) != -1:
            name = name.replace(i, '')
            return name.replace('()', '')
    return name


def format_time(string):

    if string[0] == 'P':
        string = string[1:]
    if string[0] == 'T':
        string = string[1:]
    if string.find('H') != -1:
        hours = int(string[:string.find('H')])
        string = string[string.find('H') + 1:]
    else:
        hours = 0
    if string.find('M') != -1:
        minutes = int(string[:string.find('M')])
        string = string[string.find('M') + 1:]
    else:
        minutes = 0
    if string.find('S') != -1:
        seconds = int(string[:string.find('S')])
    else:
        seconds = 0
    return hours * 3600 + minutes * 60 + seconds


def format_date(string):

    return string[:string.find('T')]


def string_to_arr(string):

    string = str(string)
    string = string.replace('[', '')
    string = string.replace(']', '')
    string = string.replace('\'', '')
    string = string.replace(' ', '')
    string = string.replace(',', ' ')
    return string.split(' ')


def remove_tags(arr):
    
    for i in range(len(arr)):
        if arr[i].find('https://en.wikipedia.org/wiki/') != -1:
            arr[i] = arr[i][30:]
    if 'Music' in arr:
        arr.remove('Music')
    return arr
