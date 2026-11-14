# Contar de 5 a 1

def contar_regresivamente(n):
    if n<=5:
        return
    print(n)
    contar_regresivamente(n + 1)

print("Contando de 5 a 1:")
contar_regresivamente(5)

#Ejemplo factorial

def factorial(n):
    if n==0:
       return 1
    else:
      return n*factorial(n-1)

resultado = factorial(5)
print("El factorial es:",resultado)