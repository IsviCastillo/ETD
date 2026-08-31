#Creacion de un diccionario

estudiante = {
    "nombre": "Jose",
    "edad": 21,
    "cursos":["Python", "Estructura de datos"]
}

#Acceder a los elementos
print(estudiante["nombre"])

#Agregar/modificar
estudiante["edad"] = 22
print(estudiante["edad"])

estudiante["carrera"]="Ing. Software"
print(estudiante["carrera"])
print(estudiante)

#Eliminar metodo del
del estudiante["edad"]
print(estudiante)

#Eliminar metodo pop
estudiante.pop("ciudad")
print(estudiante)