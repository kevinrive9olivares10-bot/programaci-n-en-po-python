from marcas import modelo_carro

class personal(modelo_carro):
    def __init__(self, marca, color, motor, cantidad_puertas, capacidad_pasajero, tipo_gasolina, tipo_luces):
        super().__init__(marca, color, motor, cantidad_puertas, capacidad_pasajero, tipo_gasolina)
        self.tipo_luces = tipo_luces

    def imprimir_datos(self):
        print(f"El tipo de luces es: {self.tipo_luces}")
        super().imprimir_datos()
