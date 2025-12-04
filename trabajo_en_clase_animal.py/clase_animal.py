class animal:
    def __init__(self,nombre,habitat,dieta):
        self.nombre=nombre
        self.habitat=habitat
        self.dieta=dieta

    def info(self):
        print(f"el nombre del animal es:{self.nombre}")
        print(f"su habitat nativa es:{self.habitat}")
        print(f"su dieta natural es:{self.dieta}")
        return "informacion encontrada"
    