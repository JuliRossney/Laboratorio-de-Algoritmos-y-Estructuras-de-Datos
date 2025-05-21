from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
linea = contents.splitlines()
for line in linea:
    print(linea)

fecha = (input("Ingrese su fecha de nacimiento (Ej: 280908 = 28 de Septiembre del 2008)"))
if fecha in linea:
    print ("¡Tu cumpleaños aparece en los primeros un millón de dígitos de pi!")
else:
    print("a")