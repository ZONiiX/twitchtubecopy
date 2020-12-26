import pathlib

# Note: 
# Changing FRAMES and or RESOULTION will heavily impact load on CPU.
# If you have a powerful enough computer you may set it to 1080p60 

# Secrets
CLIENT_ID = '1h9a14w3j4triwkcior9tny1hz4d0w'  # Twitch Client ID
OAUTH_TOKEN = 'qq4790vdv1sxdcwgbc46uysvaxxqbt'  # Twitch OAuth Token


# Paths
PATH = str(pathlib.Path().absolute())
CLIP_PATH = PATH + '\\clips\\{}\\{}'


# Video
GAMES = ['osu!', 'Just Chatting']
VIDEO_LENGTH = 10.5 # in minutes (doesn't always work for some reason)
RENDER_VIDEO = True # If downloaded clips should be rendered into one video (True/False)
FRAMES = 60 # Frames per second (30/60)
RESOLUTION = (1080, 1920) # (height, width) for 1080p: (1080, 1920)
FILE_NAME = 'rendered' # Name of the rendered video


# Other
SAVE_TO_FILE = True # If YouTube stuff should be saved to a separate file e.g. title, description & tags (True/False)
SAVE_FILE_NAME = 'youtube' # Name of the file YouTube stuff should be saved to
UPLOAD_TO_YOUTUBE = True # If the video should be uploaded to YouTube after rendering (True/False)
DELETE_CLIPS = True # If the downloaded clips should be deleted after rendering the video (True/False)
TIMEOUT = 3600 # How often it should check if it has made a video today (in seconds)


# Twitch
RETRIES = 5

# Twitch API Request Options
HEADERS = {'Accept': 'application/vnd.twitchtv.v5+json', 'Client-ID': CLIENT_ID}
PARAMS = {'period': 'day', 'language': 'en', 'limit': 100}  # 100 is max


# YouTube

# YouTube Video
TITLE = '' # If not given a title it would take the title of the first clip, and add "- *game* Highlights Twitch"
CATEGORY = 20  # 20 for Gaming


# YouTube Tags
TAGS = {
    'osu!': 'osu, osu!, tablet, ryuk, bigblack, fc, rhythm game, game, gaming, music, osu tablet',
    'Just Chatting': 'just chatting, just chatting clips, just chatting twitch clips'
    
}

# YouTube Descriptions
DESCRIPTIONS = {
    'osu!': 'osu! twitch clips\n\n{}\n',
    'Just Chatting': 'Just Chatting twitch clips \n\n{}\n'
}
# {} will be replaced with a list of streamer names
