from clase_animal import animal


class ave(animal):
    def __init__(self, nombre, habitat, dieta,comunicacion):
        super().__init__(nombre, habitat, dieta)
        self.comunicacion=comunicacion
    
    def info(self):
        print(f"su manera de comunicarse es por medio de:{self.comunicacion}")
        super().info()
        return"informacion encontrada"