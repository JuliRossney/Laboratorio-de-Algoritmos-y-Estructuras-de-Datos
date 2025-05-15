class Restaurante: 
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describe_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} ofrece comida de tipo {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto.")


restaurante1 = Restaurante("La Casa de la Pasta", "Pasta")
restaurante2 = Restaurante("La Casa de la Pizza", "Pizza")
restaurante3 = Restaurante("La Casa de la Hamburguesa", "Hamburguesa")

restaurante1.describe_restaurante()
restaurante2.describe_restaurante()
restaurante3.describe_restaurante()
