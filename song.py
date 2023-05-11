class Song():
    def __init__(self, title, publishedAT, channel_ID, url, playlist_name):
        self.title = title
        self.publishedAT = publishedAT
        self.channel_ID = channel_ID
        self.url = url
        self.playlist_name = playlist_name

    def return_dict(self):
        return {
            'title': self.title,
            'publishedAT': self.publishedAT,
            'channel_ID': self.channel_ID,
            'url': self.url,
            'playlist_name': self.playlist_name
        }