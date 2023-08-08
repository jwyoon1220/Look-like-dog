from pytube import YouTube
import os

link = input("비디오 URL 입력: \n")

formatOption = input('파일 형식 지정(mp3, ogg): ')

yt = YouTube(link)

filePath = yt.streams.filter(only_audio=True).first().download()

mp3filePath = filePath.replace('mp4', formatOption)

os.rename(filePath, mp3filePath)

print(f'r = {mp3filePath}')

