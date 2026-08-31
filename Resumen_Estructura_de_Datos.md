# Resumen de Estructura de Datos y Python

## 1. Alcance del curso revisado

En este repositorio se trabajaron principalmente los temas de:

- Fundamentos básicos de Python
- Strings o cadenas de texto
- Tuplas
- Conjuntos o sets
- Diccionarios
- Operaciones con índices, slices y listas
- Ejercicios del Cuaderno de Trabajo
- Laboratorio 1



---

## 2. Fundamentos básicos de Python

### 2.1 Clase 1: Introducción a Python
La primera clase introduce la idea de que Python es un lenguaje de programación muy sencillo y legible. Se trabajó la estructura básica del lenguaje, comentarios, impresión y el uso de variables.

Ejemplo conceptual visto:

```python
#Introduccion a Python
print("Hola")
```

También se hizo referencia a tipos de datos básicos, como:

- enteros (`int`)
- decimales (`float`)
- texto (`str`)

Aunque en el archivo aparece una línea experimental con `print(len(float))`, lo importante es la introducción al lenguaje y a la idea de que cada valor tiene un tipo.

### 2.2 Clase 4: Impresión con tabulación y formato visual
En esta clase se trabajó la presentación de datos en pantalla usando tabulaciones (`\t`) y saltos de línea (`\n`).

Ejemplo:

```python
print("Nombre\t Nota 1\tNota 2\tNota 3 \nAna  \t10 \t10 \t10 \nJosue \t9 \t8 \t7 ")
```

Esto sirve para imprimir tablas o reportes en formato legible.

### 2.3 Clase 5: Variables, input y operaciones matemáticas
Esta clase es esencial porque se trabajaron los conceptos más básicos de programación en Python.

#### Variables
```python
nombre = "Juan Perez"
edad = 32
Nacionalidad = "Cabo Verde"

print("Hola, Yo soy: " + nombre + " tengo " + str(edad) + " años y soy de " + Nacionalidad)
```

#### Input
Se usa `input()` para pedir datos al usuario:

```python
print("Bienvenid@ " + input("Ingresa tu nombre:") + " " + input("Cual es tu apellido:") + " ")
```

#### Operaciones aritméticas
```python
n1 = 5
n2 = 10
n3 = 15
n4 = 20

print("La suma de los numeros n1 y n2 es: " + str(n1+n2))
print("La resta de los numeros n3 y n4 es: " + str(n4-n3))
print("La multiplicacion de los numeros n2 y n3 es: " + str(n2*n3))
print("La division de los numeros n1 y n4 es: " + str(n1/n4))
print("La elevacion del n1 a n2 potencia es: "+str(n1**n2))
print("El numero: " + str(n3)+" es par o impar: " + str(n3%2))
```

Conceptos importantes:
- `+`, `-`, `*`, `/` para operaciones básicas
- `**` para potenciación
- `%` para módulo o residuo
- `str()` para convertir a texto cuando se concatena con un string

### 2.4 Clase 7: Listas e índices
La clase 7 se enfocó muy fuerte en listas y en cómo acceder a elementos por posición.

#### Listas
```python
estudiantes = ["Ana", "Luis", "Carlos", "María"]
print(estudiantes)
print(estudiantes[0])
```

#### Agregar y eliminar elementos
```python
estudiantes.append("Pedro")
print(estudiantes)

estudiantes.remove("Luis")
print(estudiantes)
```

#### Ejemplo con lista de mercado
```python
lista_mercado = ["manzana", "manzana", "banana", "uva", "manzana"]
print(lista_mercado[2])
lista_mercado.append("pera")
print(lista_mercado)
```

#### Índices y slicing
```python
nombre = "chepito"
print(nombre[-1])

usuario = "salome"
nuevo_usuario = "S" + usuario[1:]
print(nuevo_usuario)

producto = "Cuadernos"
print(producto[6:9])
print(producto[2:6])
print(producto[0:3])
```

Conceptos clave:
- Las listas pueden cambiarse.
- `append()` agrega al final.
- `remove()` elimina un elemento específico.
- Los índices empiezan en 0.
- `[-1]` accede al último elemento.
- `cadena[inicio:fin]` extrae una porción de texto.

### Variables y tipos
Las variables almacenan datos y pueden contener diferentes tipos:

- Enteros: int
- Decimales: float
- Texto: str
- Booleanos: bool
- Listas, tuplas, diccionarios, sets

Ejemplo:

```python
nombre = "Isvi"
edad = 20
activo = True
```

### Print, input y f-strings
Son fundamentales para mostrar mensajes y capturar información del usuario.

```python
print("Hola mundo")
print(f"Hola, Bienvenido {input('Nombres: ')}")
```

### Carácteres de escape
Cuando se desea imprimir símbolos especiales, se usan secuencias como:

```python
print("\\")
print("/")
```

Esto sirve para imprimir un backslash porque el símbolo `\` es un carácter especial en Python.

### Conceptos clave
- Python lee línea por línea.
- `print()` muestra contenido en pantalla.
- `input()` pide datos al usuario.
- `f"... {variable} ..."` permite insertar valores dentro de un texto.

---

## 3. Strings o cadenas de texto

Los strings son secuencias de caracteres y se pueden manipular de muchas formas.

### Operaciones más importantes
- Concatenación: unir textos
- Indexación: acceder a una posición
- Slicing: obtener porciones del texto
- Longitud: `len()`

Ejemplo:

```python
mensaje = "Python"
print(mensaje[0])      # P
print(mensaje[1:4])    # yth
print(len(mensaje))    # 6
```

### Ejemplos vistos
En el cuaderno de trabajo se imprimieron versos y frases con comillas internas, por ejemplo:

```python
print('Voy desde cipote entre "la yerba"')
```

### Slicing útil
```python
texto = "Universidad de Oriente - El Salvador"
print(texto[:11])     # Universidad
print(texto[-11:])    # El Salvador
print(texto[::-1])    # reversa
print(texto[::3])     # cada tercera letra
```

### Lo importante a recordar
- Los strings son inmutables.
- Se pueden recorrer carácter por carácter.
- Se usa indexación con corchetes `[]`.
- El slicing es una herramienta muy útil para extraer partes.

---

## 4. Tuplas

Las tuplas son colecciones ordenadas e inmutables.

### Características
- No se pueden modificar después de crearla.
- Se definen con paréntesis `()`.
- Permiten almacenar varios tipos de datos.
- Puedes acceder por índice.

Ejemplo:

```python
coordenadas = (13.7, -89.2)
print(coordenadas[0])
```

### Ejemplo de ejercicio
```python
frutas = ("manzana", "banana", "uva", "manzana")
print(frutas[1])
print(len(frutas))
```

### Tuplas anidadas
Las tuplas pueden contener otras tuplas:

```python
dispositivos = (('PC001', 'Servidor principal', (150, 300), 'Activo'),)
print(dispositivos[0][2][1])
```

### Lo importante a recordar
- Son útiles cuando no quieres que cambien los datos.
- `len()` cuenta la cantidad de elementos.
- Se usan para guardar datos fijos, como coordenadas, configuraciones o registros.

---

## 5. Conjuntos (sets)

Los conjuntos son colecciones de elementos no ordenados y sin duplicados.

### Características principales
- No tienen índice.
- No permiten duplicados.
- Son desordenados.
- Son mutables.
- No se pueden acceder por posición como en listas.

Ejemplo:

```python
conjunto_1 = {10, 20, 30, 40}
print(sum(conjunto_1))
print(max(conjunto_1))
print(min(conjunto_1))
```

### Métodos fundamentales

#### add()
Agrega un elemento al conjunto.

```python
set2 = {1, 2}
set2.add(3)
print(set2)
```

#### remove()
Elimina un elemento, pero si no existe, lanza error.

```python
set3 = {1, 2}
set3.remove(2)
```

#### discard()
Elimina un elemento sin generar error si no existe.

```python
set4 = {1, 2}
set4.discard(3)
```

#### pop()
Extrae un elemento aleatorio del conjunto.

```python
set5 = {1, 2}
set5.pop()
```

#### clear()
Vacía el conjunto.

```python
set6 = {1, 2}
set6.clear()
```

### Importante sobre los sets
- Los elementos no se repiten.
- El orden no está garantizado.
- Se usan cuando necesitas manejar colecciones únicas.

---

## 6. Diccionarios

Los diccionarios guardan información en pares clave:valor.

### Estructura básica
```python
persona = {
    "nombre": "Isvi",
    "edad": 20,
    "ciudad": "Pasaquina"
}
```

### Acceso a valores
```python
print(persona["nombre"])
print(persona["edad"])
```

### Agregar o modificar elementos
```python
persona["edad"] = 22
persona["carrera"] = "Ing. Software"
```

### Eliminar elementos
```python
del persona["edad"]
persona.pop("ciudad")
```

### Ejemplo visto en clase
```python
estudiante = {
    "nombre": "Jose",
    "edad": 21,
    "cursos": ["Python", "Estructura de datos"]
}

estudiante["carrera"] = "Ing. Software"
print(estudiante)
```

### Lo importante a recordar
- Las llaves son únicas.
- Se usan para representar datos con nombre y valor.
- Son muy útiles para datos de usuarios, productos o registros.

---

## 7. Listas y operaciones de acceso

Aunque en la práctica revisada no se mostró un archivo de listas principal, sí se usaron mucho en los ejercicios y en la lógica del curso.

### Definiciones clave
- Las listas son ordenadas.
- Se pueden modificar.
- Se usan con corchetes `[]`.

```python
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
print(dias[0])
print(dias[:3])
print(dias[::-1])
```

### Slicing en listas
```python
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print(dias[:3])      # Primeros 3 días
print(dias[-2:])     # Últimos 2 días
print(dias[::2])     # Días pares
print(dias[::-1])    # Orden invertido
```

### Lo importante a recordar
- Los índices comienzan en 0.
- `[:3]` toma desde el inicio hasta el índice 2.
- `[-2:]` toma los dos últimos elementos.
- `[::-1]` invierte la secuencia.

---

## 8. Ejercicios del Cuaderno de Trabajo

### 8.1 Strings
Se practicó la impresión de textos, versos y expresiones con comillas y caracteres especiales.

Ejemplo clave:

```python
print("If we could see tomorrow, what are your plans?No one can live in sorrow, ask all your friends")
```

Y también:

```python
print("\\")
print("/")
```

### 8.2 Tuplas
Se trabajaron estructuras de datos con tuplas simples y tuplas anidadas.

Ejemplo:

```python
sistema_configuracion = ("MiAplicacion", "1.0.0", "localhost", 8080, "producción")
print(sistema_configuracion[1])
print(len(sistema_configuracion))
```

Y:

```python
dispositivos = (dispositivo1, dispositivo2, dispositivo3)
print(dispositivos[1][2][1])
```

### Lo fundamental de este cuaderno
- Practicar impresión con `print()`
- Manejo de strings con comillas y caracteres especiales
- Uso de tuplas para datos fijos
- Indexación y acceso a elementos anidados

---

## 9. Laboratorio 1

### Ejercicio 1
Impresión directa de texto y cadenas literales.

### Ejercicio 3
Uso de `input()` y f-strings para crear una captura de datos del usuario:

```python
print(f"Hola, Bienvenido {input('Nombres: ')} {input('Apellidos: ')} gracias por registrarte a la materia de: {input('Materia: ')}, tu usuario para ingresar es: {input('Carnet: ')}@univo.edu.sv")
```

### Ejercicio 7
Uso de slicing con listas de días:

```python
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print(dias[:3])
print(dias[-2:])
print(dias[::-1])
print(dias[::2])
```

### Ejercicio 8
Manipulación de strings con cortes parciales y reversa:

```python
frase = "Universidad de Oriente - El Salvador"
print(frase[:11])
print(frase[-11:])
print(frase[::-1])
print(frase[::3])
```

### Ejercicio 9
Uso de tuplas para representar puntos y cálculo de distancia al origen:

```python
punto1 = (1, 2)
punto2 = (3, 4)

puntos = [punto1, punto2]
for punto in puntos:
    distancia = (punto[0] ** 2 + punto[1] ** 2) ** 0.5
    print(distancia)
```

### Lo fundamental del laboratorio
- Manejo de strings y f-strings
- Lectura de entradas con `input()`
- Slicing y extracción de partes en textos
- Trabajo con tuplas y listas
- Aplicación práctica de estructuras de datos en casos reales

---

## 10. Temas más importantes para repasar

### Debes dominar esto:

1. Variables y tipos de datos
2. `print()`, `input()` y f-strings
3. Strings: indexación, slicing, longitud
4. Tuplas: creación, acceso y propiedades inmutables
5. Sets: add, remove, discard, pop, clear
6. Diccionarios: clave-valor, acceso, modificación y eliminación
7. Índices y slicing en listas y strings
8. Escritura y lectura de datos simples con Python

### Preguntas tipo examen
- ¿Qué diferencia hay entre lista, tupla y set?
- ¿Cómo se accede a un valor de un diccionario?
- ¿Qué hace `pop()` en un set?
- ¿Cuándo conviene usar una tupla y cuándo un diccionario?
- ¿Qué es el slicing y para qué sirve?

---

## 11. Conclusión

El curso se enfocó en construir bases sólidas de Python aplicadas a estructuras de datos. Lo más importante es comprender que:

- Las listas se usan cuando necesitas ordenar y cambiar elementos.
- Las tuplas sirven para datos fijos e inmutables.
- Los sets manejan elementos únicos y no ordenados.
- Los diccionarios organizan información por clave y valor.
- Los strings y slices son esenciales para manipular textos.

Si repites estos conceptos con ejemplos sencillos, podrás resolver la mayoría de ejercicios de la materia con claridad.
