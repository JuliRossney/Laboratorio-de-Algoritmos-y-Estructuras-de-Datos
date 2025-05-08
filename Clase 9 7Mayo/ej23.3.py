def hacer_album(artista, titulo, canciones=None):
    album_musical = {}
    album_musical['artista'] = artista
    album_musical['titulo'] = titulo
    if canciones:
        album_musical['canciones'] = canciones
    return album_musical 

while True:
    print("\nIntroduce el nombre del artista (o 'salir' para terminar):")
    artista = input()
    if artista.lower() == 'salir':
        break

    print("Introduce el título del álbum:")
    titulo = input()

    print("¿Cuántas canciones tiene el álbum? (deja en blanco si no lo sabes)")
    canciones_input = input()
    if canciones_input:
        try:
            canciones = int(canciones_input)
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
    else:
        canciones = None

    album = hacer_album(artista, titulo, canciones)
    print(f"\nÁlbum creado: {album}")