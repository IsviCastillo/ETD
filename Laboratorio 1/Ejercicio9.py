# Ejercicio 9: Crear un sistema de coordenadas usando tuplas

# Crear 5 tuplas que representen coordenadas (x, y)
punto1 = (1, 2)
punto2 = (3, 4)
punto3 = (5, 6)
punto4 = (7, 8)
punto5 = (9, 10)

# Almacenar las tuplas en una lista llamada puntos
puntos = [punto1, punto2, punto3, punto4, punto5]

# Calcular la distancia de cada punto al origen (0,0)
distancias = []
for punto in puntos: # Recorre cada punto en la lista de puntos
    distancia = (punto[0] ** 2 + punto[1] ** 2) ** 0.5 
    distancias.append(distancia) # Agrega la distancia a la lista de distancias
    print("Distancia de", punto, "al origen:", distancia)

# Mostrar cuál punto está más cerca del origen
indice_min = distancias.index(min(distancias))
print("El punto más cercano al origen es:", puntos[indice_min])


