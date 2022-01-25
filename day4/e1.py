import random

list1=[12, 13, 1.3, True, "hello",13.1416]
print(random.choice(list1))
#random de un intervalo entero
print(random.randint(1,30))
#random de flotantes
print(random.random())
#random de flotantes de un intervalo
print(random.uniform(1.3,5.1))
#acotar el numero de decimales
var= round(random.uniform(1.2,2.4),4) 
print(var)
