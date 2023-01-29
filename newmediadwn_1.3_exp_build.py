import os
import yt_dlp
from yt_dlp import YoutubeDL
import pandas as pd
from urllib.parse import urlparse

def new_url():
    new_input = input("URL: ")
    new_parts = urlparse(new_input)
    new_domain_part = new_parts.netloc
    if new_domain_part == "www.youtube.com":
        youtube_download(new_input)
    else:
        sc_download(new_input)

def youtube_download(yt_url_input):
    media_format_choice = input("Media format: \n 1.Video \n 2.Audio \n Press 1 or 2 to select: " )
    if media_format_choice == "1":
        with YoutubeDL() as ydl:
            ydl.download(yt_url_input)
            if not os.path.exists("msampler_output"):
                os.makedirs("msampler_output")
            extensions = ('.mp4','.mkv','.flv','.avi','.mp3','.flac','.wav','webm','m4a')
            for file in os.listdir():
                if file.endswith(extensions):
                    if os.path.exists("msampler_output/"+file):
                        os.remove(file)
                    else:                      
                        os.rename(file,"msampler_output/"+file)  
            print("Download complete ---")
            new_url()
    elif media_format_choice == "2":       
         ydl_audio = {
            'format': 'm4a/bestaudio/best',
            'postprocessor': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav, m4a',
            }]
        }       
         with YoutubeDL(ydl_audio) as ydl:
            ydl.download(yt_url_input)
            if not os.path.exists("msampler_output"):
                os.makedirs("msampler_output")
            extensions = ('.mp4','.mkv','.flv','.avi','.mp3','.flac','.wav','webm','m4a')
            for file in os.listdir():
                if file.endswith(extensions):
                    if os.path.exists("msampler_output/"+file):
                        os.remove(file)
                    else:                      
                        os.rename(file,"msampler_output/"+file)  
         print("Download complete ---")
         new_url()
    else:
        print("Invalid input")
        new_url()

def sc_download(sc_url_input):
    with YoutubeDL() as ydl:
        ydl.download(sc_url_input)
        if not os.path.exists("msampler_output"):
            os.makedirs("msampler_output")
        extensions = ('.mp4','.mkv','.flv','.avi','.mp3','.flac','.wav','webm','m4a')
        for file in os.listdir():
            if file.endswith(extensions):
                if os.path.exists("msampler_output/"+file):
                    os.remove(file)
                else:                      
                    os.rename(file,"msampler_output/"+file)  
        print("Download complete ---")
        new_url()

new_url()


