from TAD import *
from datetime import time
from datetime import datetime

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
        
    if opc == 0:
        print("finalizando programa...")
        continuar = 0
        break
    
    #opcion 1
    elif opc == 1:
        ordenN = crearOrdenes()
        #cargamos los datos
        print("cargando orden")
        try:
            id_Maq = int(input("id de la maquina: "))
        except ValueError:
            print("valor ingresado incorrecto")
            continue
        tecnico = input("tecnico asignado: ")
        equipo = input("equipo: ")
        sector = input("sector: ")
        #ingresa una fecha en string para despues convetirla con la libreria
        fecha_str = input("Ingrese una fecha (dd/mm/yyyy): ")
        fechaProg = time.strptime(fecha_str, "%d/%m/%Y")
        hora_str = input("Ingrese una hora (hh:mm): ")
        horaInicio = time.strptime(hora_str, "%H:%M")
        cargarOrden(ordenN, id_Maq, equipo, sector, tecnico, fechaProg, horaInicio)
        lista_Ordenes.append(ordenN)
        print(verOrden(ordenN))
        print("orden cargada exitosamente")
        
    #opcion 2
    elif opc == 2:
        print("modificando cronograma...\n")
        try:
            id_Maquina = int(input("id de la maquina a modificar: "))
        except ValueError:
            print("el tipo de dat ingresado es incorrecto")
            continue
        
        fecha_str = input("Ingrese la nueva fecha (dd/mm/yyyy): ")
        nuevaFecha = time.strptime(fecha_str, "%d/%m/%Y")
        hora_str = input("Ingrese la nueva hora (hh:mm): ")
        nuevaHora = time.strptime(hora_str, "%H:%M")
        
        if modificarCronograma(lista_Ordenes, id_Maquina, nuevaFecha, nuevaHora):
            print("cronograma modificado exitosamente")
            
        else:
            print("no se encontro la maquina con el id ingresado")
    
    #opcion 3       
    elif opc == 3:
        print("cancelando tarea...")
        try:
            id_Maquina = int(input("id de la maquina a cancelar: "))
        except ValueError:
            print("dato incorrecto")
            continue

        if eliminarTarea(lista_Ordenes, id_Maquina):
            print("tarea cancelada exitosamente")
        else:
            print("no se encontró la máquina")
        
    #opcion 4
    elif opc == 4:
        print("mostrando ordenes...")
        mostrarOrdenes(lista_Ordenes)
        
    #opcion 5  
    elif opc == 5:
        pass
        
        