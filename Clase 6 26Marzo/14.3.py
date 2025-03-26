usuarios_actuales = ["meli", "cata", "vicky", "CANDE", "fefi"]
usuarios_nuevos = ["julim" , "Meli" , "cande", "lola", "agustin"]

for nuevo in usuarios_nuevos:   
    disponible = True
    nuevo = nuevo.lower()
    for actuales in usuarios_actuales:
        actuales = actuales.lower()
        if nuevo == actuales:
            print (f"{nuevo}, tenes que elegir otro nombre")
            disponible = False 
    if disponible:
        print(f"{nuevo} está disponible")