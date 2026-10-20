#if permite ejecutar un bloque de codigo solamente cuando una condicion es verdadera.

edad = 19

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
 

# Otra condicion
nota = 5.5

if nota>=9:
    print("Excelente")
elif nota>=7:
    print("Aprobado")
    #si es mayor que 5 y menor que 7
elif nota>=5 and nota<7:
    print("Se va a insuficiencia")    
else:
    print("Reprobado")


#Otra condicion

clientes = ["Ana", "Carlos", "Maria", "Jose"]

for cliente in clientes:
    print(cliente)


#for range()
for i in range(5):
 print("Hola")


#While : permite ejecutar un bloque de codigo mientras una condicion sea verdadera.

contador = 1

while contador <= 5:
    print(contador)
    contador += 1
