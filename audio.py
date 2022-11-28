import os
import sys
from pytube import YouTube
from pytube.cli import on_progress

PATH_SAVE = "/home/griffith/Music/audio/"

link = input("enter the url for your youtube video\n")
yt = YouTube(link, on_progress_callback=on_progress)

#Download mp3
audio_file = yt.streams.filter(only_audio=True).first().download(PATH_SAVE)
base, ext = os.path.splitext(audio_file)
new_file = base + '.mp3'
os.rename(audio_file, new_file)

