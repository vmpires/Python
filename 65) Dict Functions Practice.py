
def get_info(album):
    infos = [album['title'], album['artist']]
    tempos = []
    for song in album['songs']:
        tempos.append(song[1])
    infos.append(f"Maior duração: {max(tempos)} mins.")
    return (tuple(infos))

def get_length(album):
    albumlength = 0
    for song in album['songs']:
        albumlength += song[1]
    return (f"Duração total: {albumlength} mins.")

album = {
    'title':'Is This It',
    'artist':'The Strokes',
    'genre':['Indie Rock', 'Garage Rock'],
    'release year': 2001,
    'producer':'Gordon Raphael',
    'songs':[("Is This It", 2.31),
            ("The Modern Age", 3.28),
            ("Soma", 2.33),
            ("Barely Legal", 3.54),
            ("Someday", 3.03),
            ("Alone, Together", 3.08),
            ("Last Nite", 3.13),
            ("Hard to Explain", 3.44),
            ("New York City Cops", 3.31),
            ("Trying Your Luck", 3.22),
            ("Take It or Leave It", 3.16)],
    'favorite': "Alone, Together",
}

print(album['favorite'])
print(get_info(album))
print(get_length(album))