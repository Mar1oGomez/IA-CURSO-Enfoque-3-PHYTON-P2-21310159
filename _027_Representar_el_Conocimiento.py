# Definir una clase para representar animales
class Animal:
    def __init__(self, nombre, tipo_alimentacion, habitat):
        self.nombre = nombre
        self.tipo_alimentacion = tipo_alimentacion
        self.habitat = habitat

# Funci�n principal
def main():
    # Crear instancias de la clase Animal para representar diferentes animales
    leon = Animal("Le�n", "carn�voro", "sabana")
    tigre = Animal("Tigre", "carn�voro", "selva")
    elefante = Animal("Elefante", "herb�voro", "selva")

    # Imprimir informaci�n sobre los animales
    print("Informaci�n sobre los animales:")
    print("Nombre:", leon.nombre, "- Tipo de alimentaci�n:", leon.tipo_alimentacion, "- H�bitat:", leon.habitat)
    print("Nombre:", tigre.nombre, "- Tipo de alimentaci�n:", tigre.tipo_alimentacion, "- H�bitat:", tigre.habitat)
    print("Nombre:", elefante.nombre, "- Tipo de alimentaci�n:", elefante.tipo_alimentacion, "- H�bitat:", elefante.habitat)

if __name__ == "__main__":
    main()

