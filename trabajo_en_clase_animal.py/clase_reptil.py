from clase_animal import animal


class reptil(animal):
    def __init__(self,nombre,habitat,dieta,moverse):
        super().__init__(nombre,habitat,dieta)
        self.moverse=moverse
    def info(self):
        print(f"es es muy {self.moverse},para cazar en el agua")
        super().info()
        return "informacion encontrada"
        