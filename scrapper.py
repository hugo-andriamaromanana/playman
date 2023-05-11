from data import *
import requests


def get_playlist_ID_dic(ID):
    url = "https://www.googleapis.com/youtube/v3/playlists"
    params = {
        'part': 'snippet',
        'channelId': ID,
        'maxResults': 50,
        'key': PARAMS['key']
    }
    response = requests.get(url, params=params).json()
    dic = {}
    for i in range(len(response['items'])):
        dic[response['items'][i]['snippet']['title']] = response['items'][i]['id']
    while 'nextPageToken' in response.keys():
        params['pageToken'] = response['nextPageToken']
        response = requests.get(url, params=params).json()
        for i in range(len(response['items'])):
            dic[response['items'][i]['snippet']['title']] = response['items'][i]['id']
    return dic

def get_playlist_items(playlist_id):
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    params = {
        'part': 'snippet',
        'playlistId': playlist_id,
        'maxResults': 50,
        'key': PARAMS['key']
    }
    response = requests.get(url, params=params).json()
    arr = []
    arr.append(response)
    while 'nextPageToken' in arr[-1].keys():
        params['pageToken'] = arr[-1]['nextPageToken']
        response = requests.get(url, params=params).json()
        arr.append(response)
    return arr

def get_song_data(data,playlist_name,playlist_ID):
    for i in range(len(data)):
        try:
            for j in range(len(data[i]['items'])):
                song = {}   
                song['title'] = clean(data[i]['items'][j]['snippet']['title'])
                song['publishedAt'] = data[i]['items'][j]['snippet']['publishedAt']
                song['channel_ID'] = data[i]['items'][j]['snippet']['videoOwnerChannelId']
                song['url'] = data[i]['items'][j]['snippet']['resourceId']['videoId']
                song['playlist_ID'] = playlist_ID
                song['playlist_name'] = playlist_name
                add_dic_to_items_csv(song)
        except:
            pass

def scrap_playlist(playlist_ID,playlist_name):
    data = get_playlist_items(playlist_ID)
    get_song_data(data,playlist_name,playlist_ID)

def scrap_all_playlists_from():
    dic = get_playlist_ID_dic(PARAMS['channel_id'])
    for i in dic:
        scrap_playlist(dic[i],i)

scrap_playlist('PLn4GvABOzCQt4ciDfegKgW_Q6kDLfqFa-','Trash')
# scrap_all_playlists_from()