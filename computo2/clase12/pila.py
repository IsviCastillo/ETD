pila = []
pila.append("Iniciar Sesion") # append() para agregar elementos a la pila
pila.append("Consultar el perfil")
pila.append("Ver amigos en comun")
pila.append("Hola k ase?")

print("Pila actual:")
print(pila)

#Desapilar un elemento
accion = pila.pop() # pop() para eliminar el último elemento agregado a la pila

print("\nAcción retirada:")
print(accion)

print("\nPenultima Accion retirada:")
print(pila.pop())
print(pila)
