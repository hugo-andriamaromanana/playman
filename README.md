# playman

def scrap_playlist(playlist_ID):
    data = get_playlist_items(playlist_ID)
    playlist_name = get_playlist_ID_dic(PARAMS['channel_id'])[playlist_ID]
    get_song_data(data,playlist_name,playlist_ID)

def scrap_all_playlists_from_user():
    dic = get_playlist_ID_dic(PARAMS['channel_id'])
    for i in dic:
        scrap_playlist(dic[i])