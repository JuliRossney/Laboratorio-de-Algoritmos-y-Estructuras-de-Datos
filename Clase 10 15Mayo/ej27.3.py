class Usuario: 
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
    def describe_usuario(self):
        print(f"El usuario {self.nombre} {self.apellido} con email {self.email} ha iniciado sesión.")

    def saludar_usuario(self):
        print(f"Hola {self.nombre} {self.apellido}!")

usuario1 = Usuario("Juan", "Pérez", "juanperez@gmail.com")
usuario2 = Usuario("Maria", "Pérez", "mariaperez@gmail.com")

usuario1.describe_usuario()
usuario2.describe_usuario()
usuario1.saludar_usuario()
usuario2.saludar_usuario()


