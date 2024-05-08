# Programa de operaciones con conjuntos difusos

# Definir la funci�n para calcular la pertenencia a un conjunto difuso triangular
def pertenencia_triangular(x, a, b, c):
    if x <= a:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return (c - x) / (c - b)
    else:
        return 0

# Funci�n principal
def main():
    # Definir los par�metros del conjunto difuso triangular
    a = 2
    b = 5
    c = 8

    # Calcular la pertenencia de diferentes valores a este conjunto
    valores = [1, 3, 5, 6, 8, 10]
    for x in valores:
        pertenencia = pertenencia_triangular(x, a, b, c)
        print(f"El valor {x} pertenece al conjunto difuso triangular con pertenencia {pertenencia}")

if __name__ == "__main__":
    main()

