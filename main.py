import sys

from functions.scrapper import *
from functions.user_creation import *

def main(username,channel_id):
    
    if channel_id == 'None':
        channel_id = get_channel_ID(username)
    if func_new_user(username):
        create_user(username,channel_id)
        save_channel_id(username,channel_id)
    scrap_all_playlists_from_user(channel_id,username)
        
if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])