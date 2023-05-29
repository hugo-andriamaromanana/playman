import sys

from src.scrapper import *
from src.user_creation import *


def main(username, channel_id):

    if channel_id == 'None':
        channel_id = get_channel_ID(username)
    if check_new_user(username):
        mkdir_user(username)
        print(f'User: "{username}" created successfully')
        create_user(username, channel_id)
        save_channel_id(username, channel_id)
    scrap_all_playlists_from_user(channel_id, username)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
