# Programa de vigilancia de ejecuci�n y replanificaci�n

# Funci�n para simular la ejecuci�n de una tarea
def ejecutar_tarea(tarea):
    print("Ejecutando la tarea:", tarea)

# Funci�n para simular la vigilancia de ejecuci�n y replanificaci�n
def vigilancia_replanificacion():
    while True:
        tarea_actual = input("Ingrese la tarea actual: ")  # Solicitar al usuario la tarea actual
        if tarea_actual == "terminar":
            print("Programa finalizado.")
            break  # Salir del bucle si se ingresa "terminar"
        
        # Simular la ejecuci�n de la tarea actual
        ejecutar_tarea(tarea_actual)
        
        # Verificar si hay alg�n problema durante la ejecuci�n
        problema = input("Hubo alg�n problema durante la ejecuci�n (s/n)? ")
        if problema.lower() == "s":
            print("Replanificando...")
            # Simular la replanificaci�n
            nueva_tarea = input("Ingrese la nueva tarea: ")
            print("Replanificaci�n completada. Ejecutando la nueva tarea:", nueva_tarea)
        else:
            print("La ejecuci�n de la tarea fue exitosa.")

# Funci�n principal
def main():
    print("Bienvenido a la vigilancia de ejecuci�n y replanificaci�n.")
    vigilancia_replanificacion()  # Llamar a la funci�n de vigilancia de ejecuci�n y replanificaci�n

if __name__ == "__main__":
    main()

