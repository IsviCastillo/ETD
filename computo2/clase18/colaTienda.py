colaTienda = [] #creamos una cola vacia , porque esta iniciando a abrir la tienda

#Operacion ENQUEUE
#Tienda Rosita
colaTienda.append("Ana")
colaTienda.append("Carlos")
colaTienda.append("Luis")

print("Clientes de la Tienda Rosita: ", colaTienda)

#Operacion Peek
#Consultar quien es el primer cliente 
print("Siguiente cliente:", colaTienda[0])

#Operacion SIZE
#Consulta cuantos clientes hay
print("Clientes en espera:", len(colaTienda))

#Operacion DEQUEUE
#Atender al primer cliente
cliente = colaTienda.pop(0)
print("Cliente atendido:", cliente)

#Mostrar los clientes que siguen:
print("Clientes de la cola son:", colaTienda)

#Operacion rear
#Consulta quein esta al final de la cola
print("Ultimo cliente:", colaTienda[-1])

#Operacion IS EMPTY
#Comprueba si todavia hay elementos (Clientes)
cliente = colaTienda.pop(0)
cliente = colaTienda.pop(0)
if not colaTienda:
    print("No hay clientes esperando")
else:
    print("Todavia hay clientes esperando")

