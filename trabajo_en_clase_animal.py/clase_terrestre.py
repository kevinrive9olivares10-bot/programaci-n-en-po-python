from clase_animal import animal


class terrestre(animal):
    def __init__(self, nombre, habitat, dieta,color):
        super().__init__(nombre, habitat, dieta)
        self.color=color
    
    def info(self):
        print(f"su pelaje es:{self.color}")
        super().info()
        return"información encontrada"