from pytube import YouTube

# Programa recebe link do video + caminho para download
link = input ('Digite o link do video: ')
path = input ('Digite o caminho a ser salvo: ')
yt = YouTube(link)

# Mostra os detalhes do video
print('Título: ',yt.title)
print('Visualizações: ',yt.views)
print('Tamanho: ',yt.length,"segundos")

# Usa a maior resolução
ys = yt.streams.get_highest_resolution()

# Começa o download do vídeo
print('Baixando... Você receberá um aviso quando o download for finalizado.')
ys.download(path)
print('Download concluído!')

