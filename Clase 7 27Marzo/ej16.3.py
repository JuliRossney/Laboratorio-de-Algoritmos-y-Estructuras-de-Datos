lenguajes_favoritos = {
    "Juan":"Python",
    "Sara":"C",
    "Eduardo":"Rust",
    "Agustina":"C#",
}
personas = ["juli", "sara", "lu", "juan"]
for persona in personas:
    encontrado = False  
    for nombre in lenguajes_favoritos.keys():
        if persona.lower() == nombre.lower():
            encontrado = True
            break  

    if encontrado:
        print(f"{persona}, ya respondiste la encuesta, gracias")
    else:
        print(f"{persona}, participá")