# Programa de planificaci�n condicional simple

# Definir una funci�n para la planificaci�n condicional
def planificacion_condicional(objetivo, precondiciones, efectos):
    # Verificar si se cumplen todas las precondiciones
    if all(precondiciones[cond] for cond in precondiciones):
        # Si se cumplen, aplicar los efectos y alcanzar el objetivo
        for efecto in efectos:
            objetivo[efecto] = efectos[efecto]
        print("Objetivo alcanzado:", objetivo)
    else:
        print("No se cumplen todas las precondiciones. No se puede alcanzar el objetivo.")

# Funci�n principal
def main():
    # Definir el objetivo, las precondiciones y los efectos
    objetivo = {"estado": "inicial"}  # Estado inicial del objetivo
    precondiciones = {"estado": "inicial"}  # Estado inicial de las precondiciones
    efectos = {"estado": "final"}  # Efecto deseado

    # Llamar a la funci�n de planificaci�n condicional
    planificacion_condicional(objetivo, precondiciones, efectos)

if __name__ == "__main__":
    main()

