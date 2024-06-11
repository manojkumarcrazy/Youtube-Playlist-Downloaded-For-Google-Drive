from google.colab import drive
from pytube import Playlist, YouTube
import os

# Mount Google Drive
drive.mount('/content/drive')

# Set the playlist URL and destination path
playlist_url = 'YOUR_PLAYLIST_URL'
destination = '/content/drive/My Drive/YoutubeDownloads'

# Create destination folder if it doesn't exist
if not os.path.exists(destination):
    os.makedirs(destination)

# Function to download video with specified resolution
def download_video(video_url, resolution='720p'):
    yt = YouTube(video_url)
    video = yt.streams.filter(res=resolution, file_extension='mp4').first()
    
    if video:
        print(f"Downloading {yt.title} in {resolution} resolution...")
        video.download(destination)
        print(f"Downloaded {yt.title}")
    else:
        print(f"Resolution {resolution} not available for {yt.title}, downloading the highest resolution available.")
        video = yt.streams.get_highest_resolution()
        video.download(destination)
        print(f"Downloaded {yt.title} in highest available resolution.")

# Iterate over playlist and download videos
playlist = Playlist(playlist_url)

print(f"Total videos in playlist: {len(playlist.video_urls)}")

# Choose the desired resolution
desired_resolution = '720p'

for video_url in playlist.video_urls:
    download_video(video_url, resolution=desired_resolution)
