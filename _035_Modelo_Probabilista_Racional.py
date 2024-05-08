import random  # Importa la biblioteca random para generar n�meros aleatorios

# Definici�n de la clase del modelo probabilista racional
class ModeloProbabilistaRacional:
    def __init__(self, opciones):
        self.opciones = opciones  # Inicializa las opciones disponibles
        self.probabilidades = {opcion: 1 / len(opciones) for opcion in opciones}  # Inicializa las probabilidades uniformemente

    # M�todo para actualizar las probabilidades basadas en la evidencia
    def actualizar_probabilidades(self, evidencia):
        total = sum(self.probabilidades[opcion] for opcion in self.opciones)  # Calcula la suma total de las probabilidades
        for opcion in self.opciones:
            if opcion == evidencia:
                self.probabilidades[opcion] /= total  # Actualiza la probabilidad de la opci�n con la evidencia
            else:
                self.probabilidades[opcion] = 0  # Establece la probabilidad de las otras opciones a cero

    # M�todo para tomar una decisi�n basada en las probabilidades actuales
    def tomar_decision(self):
        return random.choices(self.opciones, weights=self.probabilidades.values())[0]  # Elige una opci�n basada en las probabilidades actuales

# Funci�n principal
def main():
    opciones = ["A", "B", "C"]  # Definir las opciones disponibles
    modelo = ModeloProbabilistaRacional(opciones)  # Crear una instancia del modelo probabilista racional

    # Actualizar las probabilidades basadas en una evidencia y tomar una decisi�n
    evidencia = "A"
    modelo.actualizar_probabilidades(evidencia)
    decision = modelo.tomar_decision()
    print("Decisi�n tomada:", decision)

if __name__ == "__main__":
    main()

