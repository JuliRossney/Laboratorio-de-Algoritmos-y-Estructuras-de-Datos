def hacer_album(artista, titulo, canciones=None):
    album_musical = {}
    album_musical['artista'] = artista
    album_musical['titulo'] = titulo
    if canciones:
        album_musical['canciones'] = canciones
    return album_musical

album1 = hacer_album('Wos', 'Oscuro Éxtasis')
album2 = hacer_album('Ariana Grande', 'Positions', 14)
album3 = hacer_album('Tini', 'Cupido')
album4 = hacer_album('Taylor Swift', 'Midnights', 13)

print(album1)
print(album2)
print(album3)
print(album4)


