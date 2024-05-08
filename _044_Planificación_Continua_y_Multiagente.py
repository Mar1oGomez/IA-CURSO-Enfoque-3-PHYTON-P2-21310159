# Programa de planificaci�n continua y multiagente

# Definir la funci�n de planificaci�n para un agente
def planificacion_agente(agente, tarea):
    # Simulaci�n de la planificaci�n del agente para la tarea
    print(f"El agente {agente} est� planificando la tarea: {tarea}")

# Funci�n principal
def main():
    # Lista de agentes y tareas
    agentes = ["Agente1", "Agente2", "Agente3"]
    tareas = ["Tarea1", "Tarea2", "Tarea3"]

    # Planificaci�n para cada agente y tarea
    for agente in agentes:
        for tarea in tareas:
            planificacion_agente(agente, tarea)  # Llama a la funci�n de planificaci�n para cada combinaci�n de agente y tarea

if __name__ == "__main__":
    main()

