usuarios = []
if usuarios:
    for usuario in usuarios:
        if usuario == "admin":
            print ("Hola admin, ¿Querés ver un informe de estado?")
        else:
            print (f"Hola {usuario}, gracias por volver a iniciar sesión")
else:
    print ("necesitamos nuevos usuarios")