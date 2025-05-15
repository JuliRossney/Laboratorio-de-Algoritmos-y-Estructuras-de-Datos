class PuestoDeHelados(Restaurante):
    def __init__(self, nombre_restaurante, tipo_cocina, sabores):
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabores = sabores
        self.sabores_disponibles = []

        
    