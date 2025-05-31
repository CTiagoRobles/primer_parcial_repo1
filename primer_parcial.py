# Alumno/a: _______TIAGO ROBLES_____________ Fecha: _____28/05_____
# PARTE 2 – EJERCICIO PRÁCTICO

# Contexto: Una institución educativa necesita registrar las notas de sus
# alumnos en distintos exámenes. Cada fila de una matriz representa un
# alumno y cada columna un examen.
# Requisitos Generales para Todos los Puntos:
# - Se deben modularizar todas las operaciones. No se permite resolver
# todo en el main.
# - No está permitido el uso de funciones propias de Python como max,
# min, sum, enumerate, etc.
# - La validación debe hacerse en la función de carga, verificando que
# cada nota sea un número entero entre 1 y 10.
# - Se debe implementar un menú con opciones para ejecutar cada punto
# de forma separada.
# - Usar estructuras adecuadas, acumuladores, contadores y recorrido
# doble.
# - Nombrar las funciones tal como se indican a continuación.
# 1 – Función cargar_matriz_notas(): Recibe dos enteros n y m y permite
# cargar n x m notas válidas entre 1 y 10 inclusive. La validación debe
# hacerse dentro de esta función.
# 2 – Función porcentaje_aprobados(): Calcula el porcentaje de
# exámenes aprobados (nota ≥ 6) por cada alumno y muestra un resumen
# individual. Usar contadores y acumuladores.

# Programación 1
# Gisele Milagros Gonzalez - Patricio Costello
# Parcial 1 - Tema 1

# 3 – Función mejor_promedio(): Calcula el promedio de cada alumno y
# determina cuál tiene el mejor promedio. Retorna el índice del alumno y
# el valor del promedio.
# 4 – Función buscar_nota(): Recibe la matriz y una nota buscada, y
# retorna una lista con todas las posiciones (fila, columna) donde aparece
# esa nota exacta.
"""
1  Función cargar_matriz_notas(): Recibe dos enteros n y m y permite
cargar n x m notas válidas entre 1 y 10 inclusive. La validación debe
hacerse dentro de esta función.
"""

def cargar_matriz_notas(n, m):
    """
    Objetivo: Cargar y validar notas de un examen
    m = columnas (EXAMENES)
    n = filas (ALUMNOS)
    En caso de que este conteste algo erroneo se le va a volver a preguntar.
    """
    todas_las_notas= [] #LISTA "MAIN" / principal


    for i in range(m): #M COLUMNAS = EXAMENES
        print(f"Examen {i + 1}") #i empieza en 0 asi que le sumo 1. 
        notas_almunos_guardar = []
        for j in range(n): #N FILAS = ALUMNOS
            bandera = False # utilizo bandera 
            while not bandera:
                entrada_usuario = input(f"Ingrese la nota del examen para el etudiante {j + 1}: ")
                if entrada_usuario.isdigit(): 
                    notas_alumno = int(entrada_usuario) # se verifica si es entero  y numero
                    if 1 <= notas_alumno <= 10: # verifica si la nota esta entre 1 y 10
                        break # se rompe el bucle
                    else:
                        print("ERROR: Ingrese un  numero dentro del rango (1-10)") #en caso de que no cumpla ese rango, entonces que le diga ERROR
                else:
                    print("ERROR: Ingrese un numero entero.") # en caso de que no sea entero ni numero.
            notas_almunos_guardar.append(notas_alumno) #agrego la nota de cada alumno a la lista temporal
        todas_las_notas.append(notas_almunos_guardar) #una vez termina de agregar la nota de cada alumno a la lista temporal, esta se pasan a la lista "main"
        print(f"Notas del examen {i + 1} cargadas: {notas_almunos_guardar}")
    return todas_las_notas

'''
#2 Función porcentaje_aprobados(): Calcula el porcentaje de
 exámenes aprobados (nota ≥ 6) por cada alumno y muestra un resumen
 individual. Usar contadores y acumuladores.
'''

# creo la funcion
def porcentaje_aprobados(cargar_matriz_notas):
    '''
    Objetivo : Calcular el porcentaje de examenes aprobados.
    Si el examen tiene de nota => 6 es aprobado, si tiene menos no acumula.
    En caso de que no haya notas este retorna al menu

    '''

    #Si las notas no estan cargadas, que salga de la opcion 2 y vuelva al menu.
    if not cargar_matriz_notas: 
        print("ERROR: No hay datos de notas cargados. Ingrese la opcion 1 e intente nuevamente. ")
        return
    
    alumno = 0 # contador para el numero de alumno.

    #Empiezo recorriendo las filas (alumnos):
    for fila in (cargar_matriz_notas):

        aprobados_temporal = 0 # contador de examenes aprobados 
        notas_alumnos_temporal = len(fila) #lee la cantidad de examenes del alumno
        
        for nota in fila:  #Recorre la nota de cada alumno 

            #Ahora: Si esta nota es mayor o igual a 6 entonces suma 1 aprobado, si no no suma nada.
            if nota >= 6: #Y aca ve si la nota en filas es un mayor o igual >=6.
                aprobados_temporal += 1

        porcentaje = (aprobados_temporal / notas_alumnos_temporal) * 100
        alumno += 1 # suma un alumno 

        #como resultado da la notas del alumno y el porcentaje final.
        print(f"El alumno {alumno} con las notas: {fila}. Tiene un porcentaje de {porcentaje}% examenes aprobados.")         
    return

'''
3.  Función mejor_promedio(): Calcula el promedio de cada alumno y 
    determina cuál tiene el mejor promedio. Retorna el índice del alumno y
    el valor del promedio.
'''

def mejor_promedio(cargar_matriz_notas):
    '''
    objetivo:  Calcular el mejor promedio entre todos los alumnos y retonar el numero del alumno y el promedio.
    '''
    #Si las notas no estan cargadas, la funcion se acaba
    if not cargar_matriz_notas:
        print("ERROR: No hay datos de notas cargados.")
        return
    
    #cantidad alumnos (filas)
    cantidad_alumnos = len(cargar_matriz_notas)
    #cantidad examenes (columnas)
    cantidad_examenes = len(cargar_matriz_notas[0])
    

    mejor_prom = 0  # Guarda el mejor promedio que encuentre
    mejor_indice = 0 #guarda el indice del alumno con mejor promedio
    
    for i in range(cantidad_alumnos):  #recorre las filas = alumnos 
        suma = 0
        for j in range(cantidad_examenes):  # recorre las columnas = examenes.  
            suma += cargar_matriz_notas[i][j] # sumamos notas del alumno
        #sacamos el promedio del alumno
        promedio = suma / cantidad_examenes       
        #si este promedio es mejor que el mejor promedio encotnrado hasta ahora, entonces se actualiza.
        if promedio > mejor_prom:
            mejor_prom = promedio # se actualiza si es mejor que el que encontro hasta el momento.
            mejor_indice = i + 1 #i empieza en 0 por eso le sumamos 1.
    #resultado:
    print(f"El alumno {mejor_indice} tuvo el mejor promedio: {mejor_prom}")


    return mejor_indice, mejor_prom


'''
4 Función buscar_nota(): Recibe la matriz y una nota buscada, y
retorna una lista con todas las posiciones (fila, columna) donde aparece
esa nota exacta.
'''
def buscar_nota(matriz):
    #validamos si esta la matriz.
    if not matriz: 
        print("ERROR: No hay datos de notas cargados.")
        return
    
    #nota que busque el usuario
    entrada_usuario = input("Ingrese la nota que esta buscando: ")
    
    #si esa nota es numero entonces pasa a entero
    if entrada_usuario.isdigit():
        nota = int(entrada_usuario)

        #valido si la nota esta entre 1-10
        if 1 <= nota <= 10:
            x = 0 #variable para ver si encontro numero o no

            #recorremos la matriz, primero recorriendo las filas (alumnos)
            for i in range(len(matriz)):
                #recorremos las columnas (examenes)
                for j in range(len(matriz[i])):
                    #si encuentra un elemento igual a la nota entonces GG
                    if matriz[i][j] == nota:
                        print(f"El número {nota} se encuentra en la fila {i+1} columna {j+1}")
                        x = 1 #esto avisa que si encontro numero
            if x == 0: # si no encontro numero entonces que printee que no lo encontro.
                print(f"La nota {nota} no se encuentra en la matriz.")
        else: # si no encuentra un numero dentro del 1-10
            print("ERROR: Ingrese un número dentro del rango (1-10)")
    else: # si la entrada no es un entero.
        print("ERROR: Ingrese un número entero.")
    return

def menu():
    print("Bienvenido al administrador de notas.")
    print("Ingrese la opcion que desee: ")
    print("1. Cargar notas a la nube.")
    print("2. Ver el porcentaje de alumnos aprobados individual.")
    print("3. Ver el mejor promedio.")
    print("4. Buscar una nota especifica.")
    print("0. Salir del programa")
