from pytube import YouTube
import moviepy.editor as mp
import re
import os

# Link desejado e caminho a ser salvo
link = input("Informe o link do video desejado: ")
path = input("Digite o caminho onde será salvo o mp3: ")
yt = YouTube(link)

# Realiza o download
print("Baixando...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download concluído.")

#Converte mp4 para mp3
print("Convertendo o arquivo...")
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)

print("MP3 baixado com sucesso!")