def hacer_auto(fabricante, modelo, **extra):
    extra['fabricante'] = fabricante
    extra['modelo'] = modelo
    return extra
auto = hacer_auto('Nissan', 'Versa', color='rojo', año=2016)
print(auto)

