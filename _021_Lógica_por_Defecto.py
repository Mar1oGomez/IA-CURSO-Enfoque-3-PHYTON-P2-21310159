# Programa de l�gica por defecto en Python

# Base de conocimiento inicial
base_conocimiento = {
    "puede_volar": ["p�jaro", "avi�n"],
    "puede_nadar": ["pez", "ballena"],
    "es_mamifero": ["ballena", "perro"]
}

# Funci�n para verificar si un hecho est� en la base de conocimiento
def verificar_hecho(hecho, base_conocimiento):
    for atributo, valores in base_conocimiento.items():
        if hecho in valores:
            return True
    return False

# Funci�n para inferir nuevos hechos basados en la l�gica por defecto
def inferir_hechos(hecho):
    if verificar_hecho(hecho, base_conocimiento):
        print(f"�Claro que {hecho} es cierto!")
    else:
        print(f"No estoy seguro si {hecho} es cierto.")

# Consultas
inferir_hechos("p�jaro")
inferir_hechos("pez")
inferir_hechos("perro")
inferir_hechos("avi�n")
inferir_hechos("serpiente")

