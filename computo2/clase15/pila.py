# pila = []

# #Agreguemos 3 elementos a la pila

# pila.append("A")
# pila.append("B")
# pila.append("C")

# #Mostramos la pila
# print("Pila actual:", pila)

# #agregamos dos elementos mas a la pila

# pila.append("D")
# pila.append("E")

# print("pila Actualizada:", pila);


def push(pila, elemento): #estamos creando una funcion llamada push que recibe dos parametros pila y elemento
    pila.append(elemento) # agregamos el elemento a la pila usando el metodo append

def pop(pila): #estamos creando una funcion llamada pop que recibe un parametro pila
        return pila.pop() # si no esta vacia eliminamos el ultimo elemento de la pila y lo retornamos


#creamos una pila vacia

pilas = [] # creamos una lista vacia que representara nuestra pila
push(pilas, "A") # agregamos el elemento "A" a la pila usando la funcion push
push(pilas, "B") # agregamos el elemento "B" a la pila usando la funcion push
push(pilas, "C") # agregamos el elemento "C" a la pila usando la funcion push

print("Pila actual:", pilas) # mostramos la pila actual

# para usar el metodo pop se necesita una nueva variable que guarde el valor que se elimino de la pila, ya que si no se guarda el valor se pierde y no se puede usar despues

elemento=pop(pilas) # eliminamos el ultimo elemento de la pila usando la funcion pop y lo guardamos en la variable elemento
print("Elemento eliminado:", elemento) # mostramos el elemento eliminado

# Ejercicio: Crear una pila que simule un sistema de aceleracion de un automovil, donde se agreguen elementos que representen la velocidad del automovil

def push(Vel_inicial, Inc_veL): #estamos creando una funcion llamada push que recibe dos parametros pila y elemento
    Vel_inicial.append(Inc_veL) # agregamos el elemento a la pila usando el metodo append

automovil = [] # creamos una lista vacia que representara nuestra pila de velocidades
push(automovil, 0) # agregamos la velocidad inicial del automovil (0) a la pila usando la funcion push
push(automovil,20) # agregamos la velocidad 20 a la pila usando la funcion push
push(automovil,40) # agregamos la velocidad 40 a la pila usando la funcion push
print("Velocidades del automovil:", automovil) # mostramos las velocidades del automovil


