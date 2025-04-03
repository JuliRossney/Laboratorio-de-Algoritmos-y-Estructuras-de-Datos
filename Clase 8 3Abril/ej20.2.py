pedidos_sandwiches = ["atun","jyq","pastron", "tomate y queso", "pastron", "pastron", "huevo"]
pedidos_terminados = []

print ("Nos quedamos sin pastron")


for sandwiches in pedidos_sandwiches:
    if sandwiches != "pastron":
        print (f"Preparé tu sandwich de {sandwiches}\n")
        pedidos_terminados.append(sandwiches)

print(f"Sandwiches terminados: {pedidos_terminados}")