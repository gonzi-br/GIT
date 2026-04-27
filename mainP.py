import TAD
from datetime import time
#comienzo del programa
print("---INICIALIZACION DEL PROGRAMA")

#VARIABLES
continuar = 1
lista_Ordenes = []

while continuar != 0:
    print("---menu---")
    print("1 - registrar nuevas ordenes")
    print("2 - modificar cronograma")
    print("3 - cancelar tareas")
    print("4 - mostrar todas las ordenes activas")
    print("5 - reprogramar tareas")
    print("6 - depurar")
    print("0 - finalizar")
    
    try:
        opc = int(input("opcion: "))
    except ValueError:
        print("valor ingresado incorrecto")
        continue

if opcion == 0:
    print
    