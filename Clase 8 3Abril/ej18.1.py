respuesta = int(input("¿Cuántas personas hay en tu grupo para cenar?"))
if respuesta > 8:
    print ("Van a tener que esperar por una mesa")
elif respuesta <= 8 and respuesta > 1:
    print ("Su mesa está lista")
else:
    print ("error")