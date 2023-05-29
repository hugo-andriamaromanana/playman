import os


def mkdir_user(username: str):
    os.mkdir(os.path.join(os.path.dirname(
        __file__), '..', '..', 'docs', username))
    
    print(f'User: "{username}" created successfully')
    print(
        f'Path: {os.path.join(os.path.dirname(__file__),"..","..","docs",username)}')


def init_items_in_user_DIR(username: str):
    items_path = os.path.join(os.path.dirname(
        __file__), "..", '..', 'docs', username, 'items.csv')
    
    with open(items_path, 'w') as f:
        f.write('title,publishedAt,duration,topic_categories,view_count,like_count,comment_count,tags,channel_title,playlist_name,channel_ID,playlist_ID,url\n')
        f.write('NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN\n')
    return f'User: "{username}" items.csv created successfully'
