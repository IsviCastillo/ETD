#Sistema de un banco
#Banco los manguitos

cola = [] #Cola vacia que sera ocupada  globalmente
numero_turno = 1 #Variable global para contabilizar los clientes

def registrar_cliente(nombre):
    global numero_turno

    #Generar el codigo de turno
    # T = Letra que significa turno
    # :03d minimo de digitos para rellenar son 3
    #Ejemplo: T001

    turno = f"T{numero_turno:03d}"
    cliente =[turno, nombre]
    cola.append(cliente)
    numero_turno += 1

    #Imprimimos los resultdados
    print("\nCliente registrado conrrectamente.")
    print("Turno asignado:", turno)
    print("Nombre del cliente:", nombre)

def ver_siguiente():
    if cola:
        siguiente = cola[0]
        print("Proximo cliente:")
        print("Turno del cliente:", siguiente[0])
        print("Nombre del cliente:", siguiente[1])
    else:
        #mostrar mensaje de que no hay clientes en espera
        print("\nNo hay clientes en espera.")

def atender_cliente():
    if cola:
        cliente = cola.pop(0)
        print("---Llamamanos al cliente---")
        print("Turno:", cliente[0])
        print("Cliente:", cliente[1])
    else:
        print("\nNo hay clientes que atender. =)")


def mostrar_cola():

    if not cola:
        print("\nNo hay clientes en espera.")
    else:
        for cliente in cola:
            print(cliente[0], "-", cliente[1])

        print("\nCantidad de clientes en espera:", len(cola))


        #Para saber quien es el ultimo cliente
        print("Ultimo turno en la cola:", cola[-1][0]) 





while True:
    #Vista de menu
    print("\n")
    print("Banco los Manguitos")
    print("--Menu de Turnos--")
    print("1. Registrar clientes")
    print("2. Ver proximos clientes")
    print("3. Llamar al  cliente")
    print("4. Mostrar todos clientes")
    print("5. Salir")



    opcion = input("Seleccione una opcion (Numero): ")
    if opcion == "1":
        nombre = input("Ingrese su nombre: ")
        registrar_cliente(nombre)

    elif opcion == "2":
        ver_siguiente()

    elif opcion == "3":
        atender_cliente()

    elif opcion == "4":
        mostrar_cola()
                    
    elif opcion == "5":
        print("\nSistema finalizado...")
        break

    else:
        print("\n La opcion seleccionada no existe.") 