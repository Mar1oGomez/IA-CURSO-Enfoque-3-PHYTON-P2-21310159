# Programa de ejemplo de inferencia utilizando l�gica de primer orden

# Hechos
mamifero = ["perro", "gato", "elefante"]
tiene_patas = ["perro", "gato", "elefante"]
vuela = ["p�jaro", "mariposa"]

# Reglas
def es_mamifero(animal):
    return animal in mamifero

def tiene_patas(animal):
    return animal in tiene_patas

def puede_volar(animal):
    return animal in vuela

# Funci�n para inferir caracter�sticas de un animal
def inferir_caracteristicas(animal):
    if es_mamifero(animal):
        print(animal, "es un mam�fero.")
        if tiene_patas(animal):
            print(animal, "tiene patas.")
    else:
        print(animal, "no es un mam�fero.")
        if puede_volar(animal):
            print(animal, "puede volar.")
        else:
            print(animal, "no puede volar.")

# Funci�n principal
def main():
    animal = input("Ingrese el nombre de un animal: ")
    inferir_caracteristicas(animal)

if __name__ == "__main__":
    main()

