#tads
#TAD 
#ID_maquina, id o codigo de la maquina
#team, equipo a cargo
#sector, sector encargado
#tecAsignado, tecnico asignado
#fechaProg, fecha programada para la orden
#horaInicio, horario de inicio de la orden

#obtener cada dato para cada orden, con su respectiva posicion en la lista

def obtenerId(orden):
    return orden[0]

def obtenerTeam(orden):
    return orden[1]

def obtenerSector(orden):
    return orden[2]

def obtenerTecAsignado(orden):
    return orden[3]

def obtenerFechaProg(orden):
    return orden[4]

def obtenerHoraInicio(orden):
    return orden[5]

#---para inciso 1---#

#crea una nueva orden 
def crearOrdenes():
    nuevaOrden = [0,"" ,"" ,"" , "", ""]
    #posiciones
    #0 id de la maquina, 1 equipo encargado, 2 sector, 3 tecnico asignado, 4 fecha programada, 5 horario de inicio
    return nuevaOrden

def cargarOrden(orden, ID_maquina, team, sector, tecAsignado, fechaProg, horaInicio):
    orden[0] = ID_maquina
    orden[1] = team
    orden[2] = sector
    orden[3] = tecAsignado
    orden[4] = fechaProg
    orden[5] = horaInicio
    
def verOrden(ord):
    return f"ID: {ord[0]}, equipo: {ord[1]}, sector: {ord[2]}, tecnico asignado: {ord[3]}, fecha programada: {ord[4]}, hora de inicio: {ord[5]}"
#indices, 0 id de la maquina, 1 equipo encargado, 2 sector, 3 tecnico asignado, 4 fecha programada, 5 hora de inicio


#---para inciso 2---#


#sirve para modificar el cronograma de alguna tarea, buscando el id, y cambiandole la fecha nueva y/o hora
def modificarCronograma(listaOrd, id_Maq, nuevaFecha, nuevaHora):
    for orden in listaOrd:
        if orden[0] == id_Maq:
            orden[4] = nuevaFecha
            orden[5] = nuevaHora
            return True
    return False
        
            
#---para inciso 3---#
    
    
#sirve para eliminar una tarea
def eliminarTarea(listaOrd, id_Maq):
    for orden in listaOrd:
        if orden[0] == id_Maq:
            listaOrd.remove(orden)
            return True
    return False
        
        
#---para incisio 4---#


def mostrarOrdenes(listaOrd):
    if len(listaOrd) == 0:
        print("no se encuentran registros")
        
    else:
        for orden in listaOrd:
            print(verOrden(orden))


#---para inciso 5---# al inciso este no lo entendi bien, si ven para modificar cambienlo

def cambiarFecha(orden, nuevaFecha):
    orden[4] = nuevaFecha
    


#---para inciso 6---# este fue el q menos entendi y no sabria como hacerlo

def depuracion():
    pass


def buscarMaquina(listaOrd, id_Maq):
    for orden in listaOrd:
        if orden[0] == id_Maq:
            return orden
    return None

def buscarTecnico(listaOrd, tecAsignado):
    for orden in listaOrd:
        if orden[3] == tecAsignado:
            return orden
    return None

def buscarEquipo(listaOrd, team):
    for orden in listaOrd:
        if orden[1] == team:
            return orden
    return None

def buscarSector(listaOrd, sector):
    for orden in listaOrd:
        if orden[2] == sector:
            return orden
    return None

def buscarFecha(listaOrd, fechaProg):
    for orden in listaOrd:
        if orden[4] == fechaProg:
            return orden
    return None

def buscarHora(listaOrd, horaInicio):
    for orden in listaOrd:
        if orden[5] == horaInicio:
            return orden
    return None

def buscarOrden():
    pass