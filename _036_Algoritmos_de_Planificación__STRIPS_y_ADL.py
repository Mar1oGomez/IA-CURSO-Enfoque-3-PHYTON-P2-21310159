# Programa de planificaci�n STRIPS

# Definir la clase para representar un estado del mundo
class Estado:
    def __init__(self, predicados):
        self.predicados = set(predicados)  # Inicializar los predicados del estado

    # M�todo para agregar un nuevo predicado al estado
    def agregar_predicado(self, predicado):
        self.predicados.add(predicado)

    # M�todo para eliminar un predicado del estado
    def eliminar_predicado(self, predicado):
        self.predicados.remove(predicado)

# Definir la clase para representar una acci�n
class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre  # Nombre de la acci�n
        self.precondiciones = set(precondiciones)  # Precondiciones de la acci�n
        self.efectos = set(efectos)  # Efectos de la acci�n

    # M�todo para verificar si la acci�n es aplicable en un estado dado
    def es_aplicable(self, estado):
        return self.precondiciones.issubset(estado.predicados)

    # M�todo para aplicar la acci�n en un estado dado
    def aplicar(self, estado):
        if self.es_aplicable(estado):
            for efecto in self.efectos:
                estado.agregar_predicado(efecto)
            return estado
        else:
            raise ValueError("Las precondiciones no se cumplen para aplicar la acci�n")

# Funci�n principal
def main():
    # Definir el estado inicial y el estado objetivo
    estado_inicial = Estado(["En(A, B)", "Libre(B)", "Sobre(A, C)", "Libre(C)"])
    estado_objetivo = Estado(["En(A, C)", "Libre(B)", "Sobre(B, C)", "Libre(A)"])

    # Definir las acciones disponibles
    acciones = [
        Accion("Mover(A, B, C)", ["En(A, B)", "Libre(C)"], ["En(A, C)", "Libre(B)"]),
        Accion("Mover(B, C)", ["En(B, C)", "Libre(B)"], ["En(A, C)", "Libre(A)"])
    ]

    # Aplicar las acciones hasta alcanzar el estado objetivo
    plan = []
    estado_actual = estado_inicial
    while estado_actual.predicados != estado_objetivo.predicados:
        for accion in acciones:
            if accion.es_aplicable(estado_actual):
                estado_actual = accion.aplicar(estado_actual)
                plan.append(accion.nombre)
                break

    # Imprimir el plan generado
    print("Plan generado:")
    for paso, accion in enumerate(plan):
        print(f"Paso {paso + 1}: {accion}")

if __name__ == "__main__":
    main()

