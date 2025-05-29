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

datos = []
def cargar_matriz_notas(n, m):
    """
    Objetivo: Cargar y validar notas de un examen
    m = columnas (EXAMENES)
    n = filas (ALUMNOS)
    En caso de que este conteste algo erroneo se le va a volver a preguntar.
    """
    todas_las_notas= []


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
            notas_almunos_guardar.append(notas_alumno) 
        todas_las_notas.append(notas_almunos_guardar)
        print(f"Notas del examen {i + 1} cargadas: {notas_almunos_guardar}")
    return todas_las_notas

cargar_matriz_notas(2, 5) # para testar. 5 examenes y 2 alumnos, tenia pensado pedir los datos en el main.

