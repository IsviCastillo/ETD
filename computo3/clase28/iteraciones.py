def sumar_iterativo(numero):
    resultado = 0

    for i in range(1, numero + 1):
        resultado += i
    return resultado

print(sumar_iterativo(5))  