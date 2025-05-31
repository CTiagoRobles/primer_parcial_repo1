from primer_parcial  import cargar_matriz_notas, porcentaje_aprobados, mejor_promedio, buscar_nota, menu

def main():
    matriz = None  # inicializo la variable matriz vacia

    while True:
        menu()
        entrada_usuario = input("Ingrese una opcion: ")

        if entrada_usuario.isdigit():
            opcion = int(entrada_usuario)
        else:
            print("ERROR: INGRESE UN NUMERO VALIDO.")

        match opcion:
            case 1:
                entrada_caso_1_examenes = input("Ingrese el numero de examenes: ")
                if entrada_caso_1_examenes.isdigit():
                    m = int(entrada_caso_1_examenes)
                    entrada_caso_1_alumnos = input("Ingrese el numero de alumnos: ")
                    if entrada_caso_1_alumnos.isdigit():
                        n = int(entrada_caso_1_alumnos)
                        matriz = cargar_matriz_notas(n, m) # se crea y se carga la matriz
                    else:
                        print("ERROR: Ingrese un número entero para alumnos.")
                else:
                    print("ERROR: Ingrese un número entero para exámenes.")

            case 2:
                #Se valida si la matriz ya se cargo, y aplico esto en todos los casos.
                if matriz: 
                    porcentaje_aprobados(matriz)
                else:
                    print("ERROR: Primero debe cargar la matriz (opción 1).")

            case 3:
                if matriz:
                    mejor_promedio(matriz)
                else:
                    print("ERROR: Primero debe cargar la matriz (opción 1).")

            case 4:
                if matriz:
                    buscar_nota(matriz)
                else:
                    print("ERROR: Primero debe cargar la matriz (opción 1).")

            case 0:
                print("Saliendo del programa... Goodbye")
                break #finaliza el bucle

            case _:
                #si ingresa un numero que no sea del 0-4
                print("ERROR: Ingrese una opción válida del menú.")


if __name__ == "__main__":
    main()