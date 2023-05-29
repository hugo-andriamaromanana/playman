from src.scripts.os_functions import *
from src.scripts.json_functions import get_json,dump_json


def user_exist(username: str):

    users = os.listdir(os.path.join(os.path.dirname(__file__), '..', 'docs'))

    if username not in users:
        print('New user creation...')
        return False
    return True


def add_user_to_settings(username: str, channel_id: str):

    users_json = get_json(os.path.join(os.path.dirname(
        __file__), '..', 'settings', 'users.json'))
    users_json[username] = {
        "channel_id": channel_id
    }
    dump_json(users_json, os.path.join(os.path.dirname(
        __file__), '..', 'settings', 'users.json'))
    return f'User: "{username}" added to settings/users.json'


def create_user_files(username: str, channel_id: str):

    mkdir_user(username)
    add_user_to_settings(username, channel_id)
    init_items_in_user_DIR(username)
    return f"User created successfully: \n Username: {username}\nChannel ID: {channel_id}"


def save_channel_id(username: str, channel_id: str):

    users_json = get_json(os.path.join(os.path.dirname(
        __file__), '..', 'settings', 'users.json'))
    users_json[username]['channel_id'] = channel_id
    return f'Channel ID: "{channel_id}" saved successfully for user: "{username}"'
