from TAD import *

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
    
    elif opc == 1:
        orden = crearOrdenes()
        try:
            id_Maq = int(input("ingrese el id de la maquina: "))
        except ValueError:
            print("valor ingresado incorrecto")
            continue 
        team = input("ingrese el equipo encargado: ") 
        sector = input("ingrese el sector encargado: ") 
        tecAsignado = input("ingrese el tecnico asignado: ") 
        fechaProg = input("ingrese la fecha programada: ")
        horaInicio = input("ingrese el horario de inicio: ")
        cargarOrden(orden, id_Maq, team, sector, tecAsignado, fechaProg, horaInicio)
        lista_Ordenes.append(orden)
        print("orden registrada con exito")
        print(verOrden(orden))
        
        
        
        
    elif opc == 2:
        try:            
            id_Maq = int(input("ingrese el id de la maquina: "))
        except ValueError:  
            print("valor ingresado incorrecto")
            continue
        for id in lista_Ordenes:
            if id_Maq == id["id_Maq"]:
                print(verOrden(id))
        print("ingrese nuevo cronograma\n")
        nuevaFecha = input("ingrese la nueva fecha programada: ")
        nuevaHora = input("ingrese el nuevo horario de inicio: ")
        if modificarCronograma(lista_Ordenes, id_Maq, nuevaFecha, nuevaHora):
            print("cronograma modificado con exito")
        else:
            print("no se encontro la orden con el id ingresado")
        
    
    elif opc == 3:
        try:            
            id_Maq = int(input("ingrese el id de la maquina: "))
        except ValueError:  
            print("valor ingresado incorrecto")
            continue
        for id_m in lista_Ordenes:
            if id_Maq == id_m["id_Maq"]:
                print(verOrden(id_m))
        confirmar = int(input("desea cancelar orden?) |0 no - 1 si|: "))
        if confirmar == 1:
            eliminarTarea(lista_Ordenes, id_Maq)
            print("orden cancelada exitosamente...")
        elif confirmar == 0:
            print("orden no cancelada")
                        
        
    elif opc == 4:
        mostrarOrdenes(lista_Ordenes)
        
    
    elif opc == 5:
        print("reprogramar tareas")
        
    
    elif opc == 6:
        pass