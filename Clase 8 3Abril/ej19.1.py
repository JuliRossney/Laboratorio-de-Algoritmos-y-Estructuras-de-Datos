mensaje = "\nIngresa un ingrediente que quieras para tu pizza"
mensaje += "\n(Escribí 'salir' cuando termines.) "

while True:
    ingrediente = input(mensaje)
    if ingrediente == 'salir':
        break
    else:
        print(f"Voy a agregar {ingrediente.title()} a la pizza :)")