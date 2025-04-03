while True:
    nombre = str(input("¿Cual es tu nombre? "))
    lugar = str(input("Si pudieras visitar un lugar en el mundo, ¿A dónde irías? "))
    sino = str(input("¿Hay mas usuarios?(Si/No): "))
    sino = sino.lower()
    if sino == "si":
        continue
    elif sino == "no":
        print (f"A {nombre}, le gustaría viajar a {lugar}")
        break
    else:
        "erorr"