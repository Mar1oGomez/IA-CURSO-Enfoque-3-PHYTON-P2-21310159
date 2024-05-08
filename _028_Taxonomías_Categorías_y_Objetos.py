# Definir la taxonom�a como un diccionario donde las claves son las categor�as y los valores son listas de objetos
taxonomia = {
    "Animales": ["Perro", "Gato", "Elefante"],
    "Frutas": ["Manzana", "Banana", "Naranja"],
    "Colores": ["Rojo", "Verde", "Azul"]
}

# Funci�n para imprimir la taxonom�a
def imprimir_taxonomia(taxonomia):
    for categoria, objetos in taxonomia.items():  # Iterar sobre las claves y valores del diccionario
        print(categoria + ":")  # Imprimir el nombre de la categor�a
        for objeto in objetos:  # Iterar sobre los objetos dentro de la categor�a
            print("- " + objeto)  # Imprimir cada objeto con un guion al inicio

# Funci�n principal
def main():
    print("Taxonom�a:")  # Imprimir encabezado
    imprimir_taxonomia(taxonomia)  # Llamar a la funci�n para imprimir la taxonom�a

if __name__ == "__main__":
    main()

