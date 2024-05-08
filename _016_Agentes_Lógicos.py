# Programa de un agente l�gico para resolver un problema de l�gica de primer orden

# Definir la funci�n para el agente l�gico
def agente_logico(persona, lugar, hora):
    # Reglas l�gicas para determinar la acci�n del agente
    if persona == "Juan" and lugar == "parque" and hora == "tarde":
        return "Jugar al f�tbol"  # Si Juan est� en el parque por la tarde, juega al f�tbol
    elif persona == "Mar�a" and lugar == "casa" and hora == "noche":
        return "Ver una pel�cula"  # Si Mar�a est� en casa por la noche, ve una pel�cula
    elif persona == "Pedro" and lugar == "biblioteca" and hora == "ma�ana":
        return "Estudiar"  # Si Pedro est� en la biblioteca por la ma�ana, estudia
    else:
        return "No se puede determinar la acci�n"  # Si no se cumplen las condiciones anteriores, no se puede determinar la acci�n

# Funci�n principal
def main():
    # Ejemplos de consultas al agente l�gico
    print(agente_logico("Juan", "parque", "tarde"))  # Consulta para Juan en el parque por la tarde
    print(agente_logico("Mar�a", "casa", "noche"))  # Consulta para Mar�a en casa por la noche
    print(agente_logico("Pedro", "biblioteca", "ma�ana"))  # Consulta para Pedro en la biblioteca por la ma�ana

if __name__ == "__main__":
    main()

