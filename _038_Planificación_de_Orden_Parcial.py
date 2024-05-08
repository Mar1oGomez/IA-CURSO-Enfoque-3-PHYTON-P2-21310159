# Programa de planificaci�n de orden parcial

# Definir una funci�n para la planificaci�n de orden parcial
def planificacion_orden_parcial(tareas):
    plan = []  # Inicializar el plan vac�o

    # Iterar sobre todas las tareas
    for tarea in tareas:
        # Verificar si todas las tareas previas de la tarea actual est�n en el plan
        if all(tarea_previa in plan for tarea_previa in tarea["previas"]):
            plan.append(tarea)  # Agregar la tarea al plan si todas las tareas previas est�n en el plan

    return plan  # Devolver el plan resultante

# Funci�n principal
def main():
    # Definir las tareas con sus respectivas tareas previas
    tareas = [
        {"nombre": "Tarea A", "previas": []},
        {"nombre": "Tarea B", "previas": ["Tarea A"]},
        {"nombre": "Tarea C", "previas": ["Tarea A", "Tarea B"]},
        {"nombre": "Tarea D", "previas": ["Tarea C"]},
        {"nombre": "Tarea E", "previas": ["Tarea B"]},
    ]

    # Realizar la planificaci�n de orden parcial
    plan = planificacion_orden_parcial(tareas)

    # Mostrar el plan resultante
    print("Planificaci�n de Orden Parcial:")
    for tarea in plan:
        print(tarea["nombre"])

if __name__ == "__main__":
    main()

