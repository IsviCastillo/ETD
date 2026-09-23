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

