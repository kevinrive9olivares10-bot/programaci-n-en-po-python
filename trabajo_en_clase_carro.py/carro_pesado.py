from marcas import modelo_carro


class carga(modelo_carro):
    def __init__(self, marca, color, motor, cantidad_puertas, capacidad_pasajero, tipo_gasolina,peso):
        super().__init__(marca, color, motor, cantidad_puertas, capacidad_pasajero, tipo_gasolina)
        self.peso=peso

    def imprimir_datos(self):
        print(f"su capacidad maxima de peso es:{self.peso}toneladas")
        super().imprimir_datos()
        return "información encontrada"

