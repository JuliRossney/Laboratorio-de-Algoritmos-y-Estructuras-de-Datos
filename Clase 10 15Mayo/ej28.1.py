class Restaurante: 
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.clientes_atendidos = 0

    def describe_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} ofrece comida de tipo {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto.")

    def establecer_clientes_atendidos(self, cantidad):
        self.clientes_atendidos = cantidad

    def incrementar_clientes_atendidos(self, cantidad):
        self.clientes_atendidos += cantidad

nombre_restaurante = "La Casa de la Pasta"
tipo_cocina = "Pasta"
restaurante = Restaurante(nombre_restaurante, tipo_cocina)

restaurante.describe_restaurante()
restaurante.abrir_restaurante()

print(f"Clientes atendidos: {restaurante.clientes_atendidos}")

restaurante.clientes_atendidos = 15
print(f"Clientes atendidos: {restaurante.clientes_atendidos}")
restaurante.establecer_clientes_atendidos(20)
print(f"Clientes atendidos: {restaurante.clientes_atendidos}")
restaurante.incrementar_clientes_atendidos(5)
print(f"Clientes atendidos: {restaurante.clientes_atendidos}")
