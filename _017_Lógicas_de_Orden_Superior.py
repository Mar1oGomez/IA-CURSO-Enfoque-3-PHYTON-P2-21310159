# Programa que utiliza l�gica de orden superior para aplicar una funci�n a una lista de elementos

# Definir una funci�n de orden superior que aplica una funci�n dada a cada elemento de una lista
def aplicar_funcion_a_lista(funcion, lista):
    # Inicializar una lista vac�a para almacenar los resultados
    resultados = []
    # Iterar sobre cada elemento de la lista
    for elemento in lista:
        # Aplicar la funci�n dada al elemento y agregar el resultado a la lista de resultados
        resultados.append(funcion(elemento))
    # Devolver la lista de resultados
    return resultados

# Funci�n de ejemplo que eleva al cuadrado un n�mero
def cuadrado(x):
    return x ** 2

# Funci�n de ejemplo que duplica un n�mero
def duplicar(x):
    return x * 2

# Funci�n principal
def main():
    # Lista de n�meros de ejemplo
    numeros = [1, 2, 3, 4, 5]

    # Aplicar la funci�n cuadrado a la lista de n�meros
    resultado_cuadrado = aplicar_funcion_a_lista(cuadrado, numeros)
    print("Aplicar cuadrado a la lista:", resultado_cuadrado)

    # Aplicar la funci�n duplicar a la lista de n�meros
    resultado_duplicar = aplicar_funcion_a_lista(duplicar, numeros)
    print("Aplicar duplicar a la lista:", resultado_duplicar)

if __name__ == "__main__":
    main()

