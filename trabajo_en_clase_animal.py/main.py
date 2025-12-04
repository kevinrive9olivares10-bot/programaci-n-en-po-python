
from clase_acuatico import acuatico
from clase_animal import animal
from clase_ave import ave
from clase_insecto import insecto
from clase_reptil import reptil
from clase_terrestre import terrestre


object=animal("hipopotamo","terrestre","hervivoro")
object.info()
print("-----------------------------------------------")
object1=reptil("cocodrilo","semiacuatico","carnivoro","rapido")
object1.info()
print("---------------------------------------------------------")
object2=terrestre("caballo","terrestre","hervivoro","negro")
object2.info()
print("---------------------------------------------------------")
object3=insecto("Escarabajo","terrestre","hervivoro","sexual")
object3.info()
print("---------------------------------------------------------")
object4=ave("halcon","aire","carnivoro","sonidos")
object4.info()
print("---------------------------------------------------------")
object5=acuatico("pez payaso","acuatico","omnívoro","sonido")
object5.info()