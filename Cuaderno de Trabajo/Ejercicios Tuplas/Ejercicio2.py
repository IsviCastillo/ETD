# Ejercicio 2

dispositivo1 = ("PC001", "Servidor principal", (150, 300), "Activo")
dispositivo2 = ("PC002", "Router", (200, 400), "Inactivo")
dispositivo3 = ("PC003", "Switch", (250, 500), "Activo")

dispositivos = (dispositivo1, dispositivo2, dispositivo3)
print(dispositivos[1][2][1])


# Solo como muestra de como se ve
print("Código:", dispositivo1[0])
print("Nombre:", dispositivo1[1])
print("Coordenada X:", dispositivo1[2][0])
print("Coordenada Y:", dispositivo1[2][1])
print("Estado:", dispositivo1[3])
