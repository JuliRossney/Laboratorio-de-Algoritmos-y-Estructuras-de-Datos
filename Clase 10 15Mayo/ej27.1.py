class Restaurante: 
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describe_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} ofrece comida de tipo {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto.")

nombre_restaurante = "La Casa de la Pasta"
tipo_cocina = "Pasta"
restaurante = Restaurante(nombre_restaurante, tipo_cocina)
restaurante.describe_restaurante()
restaurante.abrir_restaurante()
