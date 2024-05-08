# Definir la base de conocimientos
base_conocimientos = {
    "ave(vencejo)": True,     # Los vencejos son aves
    "vuela(vencejo)": True,   # Los vencejos vuelan
    "vuela(pinguino)": False, # Los ping�inos no vuelan
    "ave(pinguino)": True     # Los ping�inos son aves
}

# Definir el razonador no monot�nico
def razonador_no_monotonico(consulta):
    # Verificar si la consulta est� en la base de conocimientos
    if consulta in base_conocimientos:
        return base_conocimientos[consulta] # Si la consulta est� en la base de conocimientos, devuelve el valor asociado
    else:
        # Regla de predicci�n no monot�nica: Si no hay informaci�n expl�cita, asumir que un ave vuela
        if "ave" in consulta:
            return True # Si la consulta implica que un animal es un ave, asume que vuela
        else:
            return "No se puede determinar" # Si no se puede determinar, devuelve un mensaje indicando que no se puede determinar

# Funci�n principal
def main():
    # Ejemplos de consultas al razonador no monot�nico
    print("�El vencejo vuela?", razonador_no_monotonico("vuela(vencejo)")) # Consulta si el vencejo vuela
    print("�El ping�ino vuela?", razonador_no_monotonico("vuela(pinguino)")) # Consulta si el ping�ino vuela
    print("�El ping�ino es un ave?", razonador_no_monotonico("ave(pinguino)")) # Consulta si el ping�ino es un ave
    print("�El gorri�n vuela?", razonador_no_monotonico("vuela(gorrion)")) # Consulta sobre un gorri�n no presente en la base de conocimientos

if __name__ == "__main__":
    main()

