


class modelo_carro:
    
    def __init__(self, marca,color,motor,cantidad_puertas,capacidad_pasajero,tipo_gasolina):
        self.marca = marca
        self.color = color
        self.motor = motor
        self.cantidad_puertas = cantidad_puertas
        self.capacidad_pasajero = capacidad_pasajero
        self.tipo_gasolina = tipo_gasolina

    def imprimir_datos(self):
        print(f"La marca es {self.marca}")
        print(f"El color es: {self.color}")
        print(f"Tiene un motor {self.motor}")
        print(f"Tiene {self.cantidad_puertas} puertas")
        print(f"Tiene capacidad para {self.capacidad_pasajero} pasajeros")
        print(f"Su tipo de gasolina es {self.tipo_gasolina}")
