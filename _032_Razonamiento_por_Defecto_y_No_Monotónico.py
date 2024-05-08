# Programa de razonamiento por defecto y no monot�nico

# Definir una funci�n para verificar si un ave es un ping�ino
def es_pinguino(ave):
    # Lista de caracter�sticas comunes de los ping�inos
    caracteristicas_comunes = ["nadar", "plumas", "pico corto"]

    # Si todas las caracter�sticas comunes est�n presentes en el ave, entonces es un ping�ino
    if all(caracteristica in ave for caracteristica in caracteristicas_comunes):
        return True
    else:
        return False

# Definir una funci�n para verificar si un ave es un �guila
def es_aguila(ave):
    # Lista de caracter�sticas comunes de las �guilas
    caracteristicas_comunes = ["volar", "garras", "pico afilado"]

    # Si todas las caracter�sticas comunes est�n presentes en el ave, entonces es un �guila
    if all(caracteristica in ave for caracteristica in caracteristicas_comunes):
        return True
    else:
        return False

# Definir una funci�n para identificar el ave desconocida
def identificar_ave(ave):
    if es_pinguino(ave):  # Verificar si el ave tiene caracter�sticas de ping�ino
        return "El ave es un ping�ino."
    elif es_aguila(ave):  # Verificar si el ave tiene caracter�sticas de �guila
        return "El ave es un �guila."
    else:
        return "No se puede identificar el tipo de ave."

# Funci�n principal
def main():
    # Ejemplos de aves para identificar
    ave1 = ["nadar", "plumas", "pico corto"]  # Ping�ino
    ave2 = ["volar", "garras", "pico afilado"]  # �guila
    ave3 = ["nadar", "garras"]  # Ave desconocida

    # Identificar las aves
    print(identificar_ave(ave1))
    print(identificar_ave(ave2))
    print(identificar_ave(ave3))

if __name__ == "__main__":
    main()

