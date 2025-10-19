import os
import json
import sys
import time

# script to download videos from a youtube playlist using yt-dlp
# load .json file with videos urls, names and folder to save them
# example:
# {
#     "videos": [
#         {
#             "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
#             "name": "Rick Astley - Never Gonna Give You Up.mp4",
#         }
#     ],
#     "folder": "/some/folder",
#     "referer": "https://some.referer.com"
# }
#
# how to execute:
# python video_downloader.py videos.json


# first, load the json file from the argument
json_file_path = sys.argv[1]

# load the json file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# get the videos list
videos = data['videos']
referer = data['referer']
folder = data['folder']

# download the videos using yt-dlp
for video in videos:
    url = video['url']
    name = video['name']

    # download the video
    os.system(f"yt-dlp {url} --add-header 'Referer: {referer}' -o '{folder}/{name}'")

    # check if the video was downloaded
    if not os.path.exists(f"{folder}/{name}"):
        print(f"Error downloading video {name}")
        continue
    
    # wait 1 second
    time.sleep(1)