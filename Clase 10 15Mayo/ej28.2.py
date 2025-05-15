class Usuario: 
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.intentos_login = 0

    def describe_usuario(self):
        print(f"El usuario {self.nombre} {self.apellido} con email {self.email} ha iniciado sesión.")

    def saludar_usuario(self):
        print(f"Hola {self.nombre} {self.apellido}!")

    def incrementar_intentos_login(self):
        self.intentos_login += 1

    def reiniciar_intentos_login(self):
        self.intentos_login = 0


usuario = Usuario("Juan", "Pérez", "juanperez@gmail.com")

usuario.describe_usuario()
usuario.saludar_usuario()

usuario.incrementar_intentos_login()
usuario.incrementar_intentos_login()
usuario.incrementar_intentos_login()

print(f"Intentos de login: {usuario.intentos_login}")

usuario.reiniciar_intentos_login()
print(f"Intentos de login tras reiniciar: {usuario.intentos_login}")
