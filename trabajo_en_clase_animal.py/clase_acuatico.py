from clase_animal import animal


class acuatico(animal):
    def __init__(self, nombre, habitat, dieta,instintos):
        super().__init__(nombre, habitat, dieta)
        self.instintos=instintos

    def info(self):
       print(f"este animal tiene un instinto de, {self.instintos},muy avanzados")
       super().info()
       return"informacion encontrada"