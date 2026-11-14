# Queremos sumar los numeros desde 1 hasta un numero dado
def recursividad(i):
    if i <= 5:
        print(i)
        return i + recursividad(i + 1)
    else:
        return 0

print("La suma de los numeros del 1 al 5 es:", recursividad(1))


