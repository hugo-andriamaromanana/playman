import requests

from functions.data.format_data import *

from functions.data.json_functions import get_json
from functions.data.pandas_functions import get_csv, add_dic_to_items_csv
from functions.data.os_functions import *

PARAMS = get_json(os.path.join(os.path.dirname(__file__),'..','settings','params.json'))


def get_channel_ID(username):
    users = get_json(os.path.join(os.path.dirname(__file__),'..','settings','users.json'))
    return users[username]['channel_id']

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
            dic[response['items'][i]['snippet']
                ['title']] = response['items'][i]['id']
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


def more_metadata(url):
    url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,topicDetails,statistics&id={url}&key={PARAMS["key"]}'
    response = requests.get(url).json()
    meta_data = {}
    try:
        meta_data['duration'] = response['items'][0]['contentDetails']['duration']
    except:
        meta_data['duration'] = 'NaN'
    try:
        meta_data['publishedAt'] = response['items'][0]['snippet']['publishedAt']
    except:
        meta_data['publishedAt'] = 'NaN'
    try:
        meta_data['topic_categories'] = response['items'][0]['topicDetails']['topicCategories']
    except:
        meta_data['topic_categories'] = 'NaN'
    try:
        meta_data['view_count'] = response['items'][0]['statistics']['viewCount']
    except:
        meta_data['view_count'] = 'NaN'
    try:
        meta_data['like_count'] = response['items'][0]['statistics']['likeCount']
    except:
        meta_data['like_count'] = 'NaN'
    try:
        meta_data['comment_count'] = response['items'][0]['statistics']['commentCount']
    except:
        meta_data['comment_count'] = 'NaN'
    try:
        meta_data['tags'] = response['items'][0]['snippet']['tags']
    except:
        meta_data['tags'] = 'NaN'
    try:
        meta_data['channel_title'] = response['items'][0]['snippet']['channelTitle']
    except:
        meta_data['channel_title'] = 'NaN'
    return meta_data

def get_all_titles(playlist_name,current_user):
    df = get_csv(os.path.join(os.path.dirname(__file__),'..','users',current_user,'items.csv'))
    return list(df['title'].loc[df['playlist_name'] == playlist_name])

def get_song_data(data, playlist_name, playlist_ID, current_user):

    all_titles = get_all_titles(playlist_name,current_user)

    count_titles=0

    count = 0

    for i in range(len(data)):
        try:

            for j in range(len(data[i]['items'])):

                url = data[i]['items'][j]['snippet']['resourceId']['videoId']


                song = {}

                song['title'] = clean_title(
                    data[i]['items'][j]['snippet']['title']).strip()

                if song['title'] in all_titles:
                    count_titles+=1
                    continue
            
                meta_data = more_metadata(url)

                song['publishedAt'] = format_date(meta_data['publishedAt'])
                song['duration'] = format_time(meta_data['duration'])
                song['topic_categories'] = str(remove_tags(string_to_arr(meta_data['topic_categories'])))
                song['view_count'] = meta_data['view_count']
                song['like_count'] = meta_data['like_count']
                song['comment_count'] = meta_data['comment_count']
                song['tags'] = meta_data['tags']
                song['channel_title'] = meta_data['channel_title']
                song['playlist_name'] = playlist_name
                song['channel_ID'] = data[i]['items'][j]['snippet']['videoOwnerChannelId']
                song['playlist_ID'] = playlist_ID
                song['url'] = url

                if add_dic_to_items_csv(song,current_user):
                    print(
                        f'[SUCCESS]: {data[i]["items"][j]["snippet"]["title"]} added to database')
                    count += 1

        except:

            print(
                f'[ERROR]: {data[i]["items"][j]["snippet"]["title"]} not added to database')
            pass

    print(f'[SUCCESS]: {count_titles} songs already in database from {playlist_name}')
    print(f'[SUCCESS]: {count} songs added to database from {playlist_name}')


def scrap_playlist(playlist_ID, playlist_name, current_user):
    data = get_playlist_items(playlist_ID)
    get_song_data(data, playlist_name, playlist_ID, current_user)
    print(f'[SUCCESS]: {playlist_name} scrapped')


def scrap_all_playlists_from_user(channel_id, current_user):
    dic = get_playlist_ID_dic(channel_id)
    for i in dic:
        scrap_playlist(dic[i], i, current_user)