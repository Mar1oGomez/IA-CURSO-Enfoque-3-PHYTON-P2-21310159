# Definir una clase para representar animales
class Animal:
    def __init__(self, nombre, tipo_alimentacion, habitat):
        self.nombre = nombre
        self.tipo_alimentacion = tipo_alimentacion
        self.habitat = habitat

# Función principal
def main():
    # Crear instancias de la clase Animal para representar diferentes animales
    leon = Animal("León", "carnívoro", "sabana")
    tigre = Animal("Tigre", "carnívoro", "selva")
    elefante = Animal("Elefante", "herbívoro", "selva")

    # Imprimir información sobre los animales
    print("Información sobre los animales:")
    print("Nombre:", leon.nombre, "- Tipo de alimentación:", leon.tipo_alimentacion, "- Hábitat:", leon.habitat)
    print("Nombre:", tigre.nombre, "- Tipo de alimentación:", tigre.tipo_alimentacion, "- Hábitat:", tigre.habitat)
    print("Nombre:", elefante.nombre, "- Tipo de alimentación:", elefante.tipo_alimentacion, "- Hábitat:", elefante.habitat)

if __name__ == "__main__":
    main()

