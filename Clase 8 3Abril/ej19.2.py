mensaje = "¿Cuál es la edad de la persona? "

while True:
    edad = int(input(mensaje))
    if edad < 3:
        print ("La entrada es gratis")
    elif edad >= 3 and edad < 12:
        print ("La entrada cuesta $10")
    elif edad >= 12 and edad < 110:
        print ("La entrada cuesta $15")
    else:
        print("??")
