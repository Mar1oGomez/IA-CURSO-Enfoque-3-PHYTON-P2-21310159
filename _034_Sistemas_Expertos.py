# Sistema experto simple para determinar si alguien est� calificado para un trabajo

# Definir la base de conocimientos con reglas
base_conocimientos = {
    "experiencia": {
        "Juan": 5,
        "Mar�a": 3,
        "Pedro": 2
    },
    "educacion": {
        "Juan": "Licenciatura",
        "Mar�a": "Maestr�a",
        "Pedro": "Bachillerato"
    },
    "edad": {
        "Juan": 30,
        "Mar�a": 35,
        "Pedro": 25
    }
}

# Funci�n para evaluar si alguien est� calificado para el trabajo
def sistema_experto(nombre):
    experiencia = base_conocimientos["experiencia"][nombre]
    educacion = base_conocimientos["educacion"][nombre]
    edad = base_conocimientos["edad"][nombre]

    if experiencia >= 3 and educacion in ["Licenciatura", "Maestr�a"] and edad >= 25:
        return f"{nombre} est� calificado para el trabajo."
    else:
        return f"{nombre} no est� calificado para el trabajo."

# Funci�n principal
def main():
    # Ejemplos de consultas al sistema experto
    print(sistema_experto("Juan"))  # Consulta para Juan
    print(sistema_experto("Mar�a"))  # Consulta para Mar�a
    print(sistema_experto("Pedro"))  # Consulta para Pedro

if __name__ == "__main__":
    main()

