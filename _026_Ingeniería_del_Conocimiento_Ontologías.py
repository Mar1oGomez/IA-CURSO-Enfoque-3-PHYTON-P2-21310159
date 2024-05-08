# Definir una clase para representar una ontolog�a simple
class Ontologia:
    def __init__(self):
        self.conocimiento = {}  # Inicializar el diccionario para almacenar el conocimiento

    # M�todo para agregar relaciones a la ontolog�a
    def agregar_relacion(self, concepto, relacion, valor):
        if concepto not in self.conocimiento:
            self.conocimiento[concepto] = {}  # Inicializar un diccionario para el concepto si no existe
        self.conocimiento[concepto][relacion] = valor  # Agregar la relaci�n y su valor al diccionario del concepto

    # M�todo para consultar relaciones en la ontolog�a
    def consultar_relacion(self, concepto, relacion):
        if concepto in self.conocimiento and relacion in self.conocimiento[concepto]:
            return self.conocimiento[concepto][relacion]  # Devolver el valor de la relaci�n si existe
        else:
            return "No se encontr� la relaci�n"  # Devolver un mensaje si la relaci�n no existe

# Funci�n principal
def main():
    ontologia = Ontologia()  # Crear una instancia de la ontolog�a

    # Agregar relaciones a la ontolog�a
    ontologia.agregar_relacion("Perro", "es_un", "Animal")
    ontologia.agregar_relacion("Gato", "es_un", "Animal")
    ontologia.agregar_relacion("Animal", "tiene", "Patas")
    ontologia.agregar_relacion("Perro", "tiene", "Cola")

    # Consultar relaciones en la ontolog�a
    print(ontologia.consultar_relacion("Perro", "es_un"))  # Consulta si "Perro" es un "Animal"
    print(ontologia.consultar_relacion("Gato", "tiene"))   # Consulta si "Gato" tiene algo
    print(ontologia.consultar_relacion("Ave", "es_un"))    # Consulta si "Ave" es un "Animal" (no est� en la ontolog�a)

if __name__ == "__main__":
    main()

