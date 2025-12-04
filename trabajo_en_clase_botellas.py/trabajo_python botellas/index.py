from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico
from modelo_botella_vidrio import botella_vidrio

#Codigo principal
#Aqui va la logica del negocio
#Instancia del padre
objBotella = Botella("Coca-Cola", "1 Litro", "Especial")
objBotella.imprimir_info()
print("--------------")

#Instancia hija
objBotella_plastico = Botella_plastico("Pepsi", "500 ml", "Normal", "Redondo", "Plastico", "Sin tinte")
dato_out = objBotella_plastico.imprimir_info()
print(dato_out)
print("--------------")

objBotella_vidrio = botella_vidrio("Fanta", "750 ml", "Normal", "Grande", "Si")
objBotella_vidrio.info_vidrio()
print("--------------")
