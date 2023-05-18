from data import get_json

def clean_title(name):
    trash = get_json('/home/hugo/music/playman/database/trash.json')
    for i in trash:
        if name.find(i) != -1:
            name=name.replace(i, '')
            return name.replace('()','')
    return name

