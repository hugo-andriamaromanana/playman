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

def more_metadata(url):
    url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,topicDetails,statistics&id={url}&key={PARAMS["key"]}'
    response = requests.get(url).json()
    return {
        'duration': response['items'][0]['contentDetails']['duration'],
        'publishedAt': response['items'][0]['snippet']['publishedAt'],
        'topic_categories': response['items'][0]["topicDetails"]['topicCategories'],
        'view_count': response['items'][0]['statistics']['viewCount'],
        'like_count': response['items'][0]['statistics']['likeCount'],
        'comment_count': response['items'][0]['statistics']['commentCount'],
        'tags': response['items'][0]['snippet']['tags'],
        'channel_title': response['items'][0]['snippet']['channelTitle']
    }

def get_song_data(data,playlist_name,playlist_ID):

    count=0

    for i in range(len(data)):
        try:

            for j in range(len(data[i]['items'])):

                url=data[i]['items'][j]['snippet']['resourceId']['videoId']

                meta_data= more_metadata(url)

                song = {}   
                song['title'] = clean(data[i]['items'][j]['snippet']['title'])
                song['publishedAt'] = meta_data['publishedAt']
                song['duration'] = meta_data['duration']
                song['topic_categories'] = meta_data['topic_categories']
                song['view_count'] = meta_data['view_count']
                song['like_count'] = meta_data['like_count']
                song['comment_count'] = meta_data['comment_count']
                song['tags'] = meta_data['tags']
                song['channel_title'] = meta_data['channel_title']
                song['playlist_name'] = playlist_name
                song['channel_ID'] = data[i]['items'][j]['snippet']['videoOwnerChannelId']
                song['playlist_ID'] = playlist_ID
                song['url'] = url

                if add_dic_to_items_csv(song):
                    count+=1

        except:

            print(f'[ERROR]: {data[i]["items"][j]["snippet"]["title"]} not added to database')
            pass

    print(f'[SUCCESS]: {count} songs added to database from {playlist_name}')


def scrap_playlist(playlist_ID,playlist_name):
    data = get_playlist_items(playlist_ID)
    get_song_data(data,playlist_name,playlist_ID)
    print(f'[SUCCESS]: {playlist_name} scrapped')

def scrap_all_playlists_from():
    dic = get_playlist_ID_dic(PARAMS['channel_id'])
    for i in dic:
        scrap_playlist(dic[i],i)

# # scrap_playlist('PLn4GvABOzCQt4ciDfegKgW_Q6kDLfqFa-','Trash')
# scrap_all_playlists_from()
