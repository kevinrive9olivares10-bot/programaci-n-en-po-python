from marcas import modelo_carro

class deportivo(modelo_carro):
    def __init__(self, marca, color, motor, cantidad_puertas, capacidad_pasajero, tipo_gasolina, tipo_manejo):
        super().__init__(marca, color, motor, cantidad_puertas, capacidad_pasajero, tipo_gasolina)
        self.tipo_manejo = tipo_manejo

    def imprimir_datos(self):
        print(f"Tipo de manejo: {self.tipo_manejo}")
        super().imprimir_datos()
        return "Información encontrada"