# Programa para simular la l�gica temporal

# Definir una funci�n para verificar si es ma�ana
def es_manana(hora):
    return hora < 12  # Devuelve True si la hora es antes del mediod�a, False en caso contrario

# Definir una funci�n para verificar si es tarde
def es_tarde(hora):
    return 12 <= hora < 18  # Devuelve True si la hora est� entre el mediod�a y las 6 p.m., False en caso contrario

# Funci�n principal
def main():
    # Ejemplos de consultas para la l�gica temporal
    hora_actual = 10  # Hora actual, por ejemplo, 10 a.m.
    
    if es_manana(hora_actual):
        print("Es ma�ana.")
    elif es_tarde(hora_actual):
        print("Es tarde.")
    else:
        print("Es noche.")

if __name__ == "__main__":
    main()

