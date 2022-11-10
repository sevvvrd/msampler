import os
import random
import yt_dlp
from yt_dlp import YoutubeDL
import pandas as pd
from urllib.parse import urlparse
from pytube import YouTube

def new_url():
    new_input = input("URL: ")
    new_parts = urlparse(new_input)
    new_domain_part = new_parts.netloc
    if new_domain_part == "www.youtube.com":
        youtube_download(new_input)
    else:
        sc_download(new_input)

def youtube_download(yt_url_input):
    media_format_choice = input("Youtube link detected, \n 1.Video \n 2.Audio \n Press 1 or 2 to select: " )
    if media_format_choice == "1":
        with YoutubeDL() as ydl:
            ydl.download(yt_url_input)
            print("Download complete ---")
            new_url()
    elif media_format_choice == "2":
        audio_link = YouTube(yt_url_input)
        audio_dwn = audio_link.streams.filter(only_audio=True).first()
        out_file = audio_dwn.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + " [" + str(random.randint(1000000000, 9999999999)) + "]" + ".wav" 
        os.rename(out_file, new_file)
        print("Download complete ---")
        new_url()
    else:
        print("Invalid input")
        new_url()

def sc_download(sc_url_input):
    with YoutubeDL() as ydl:
        ydl.download(sc_url_input)
        print("Download complete ---")
        new_url()

sc_url = input("URL: ")
parts = urlparse(sc_url)
domain_part = parts.netloc

def part_analyze(domain):
    if domain == "www.youtube.com":
        youtube_download(sc_url)
    else:
        sc_download(sc_url)

part_analyze(domain_part)