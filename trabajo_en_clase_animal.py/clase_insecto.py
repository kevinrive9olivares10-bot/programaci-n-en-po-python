from clase_animal import animal

class insecto(animal):

    def __init__(self, nombre, habitat, dieta, reproduccion):
        super().__init__(nombre, habitat, dieta)
        self.reproduccion = reproduccion

    def info(self):
        print(f"Su reproducción es: {self.reproduccion}")
        super().info()
        return"informacion encontrada"
