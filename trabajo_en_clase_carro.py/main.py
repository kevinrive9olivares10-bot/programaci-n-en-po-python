from carro_pesado import carga
from marcas import modelo_carro
from carro_deportivo import deportivo
from carro_personal import personal





objcarroprincipal = modelo_carro("Nissan", "Amarillo", "v5", 4, 4, "Extra")
objcarroprincipal.imprimir_datos()

print("-------------------")

objcarro = deportivo("BMW", "Rojo", "motor 2.0", 3, 4, "Extra", "Sport")
objcarro.imprimir_datos()

print("----------------------------------------------------------------")
objcarro2=carga("volqueta","negro","v8",2,2,"extra",2)
objcarro2.imprimir_datos()
print("----------------------------------------------------------------------")
objcarro3=personal("toyota","blanca","motor2,0",3,4,"extra","led")
objcarro3.imprimir_datos()



