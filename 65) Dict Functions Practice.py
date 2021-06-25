
def get_infos(album):
    temp = []
    for i in range(len(album['songs'])):
        temp.append(album['songs'][i][1])
    indice = temp.index(max(temp))
    tupla = (album['title'], album['artist'], album['songs'][indice])
    return(tupla)

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
print(get_infos(album))
