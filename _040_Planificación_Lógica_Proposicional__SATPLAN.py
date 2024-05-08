from pysat.solvers import Minisat22 # Importar el solucionador Minisat22 desde la biblioteca PySAT

# Funci�n para resolver un problema de SAT utilizando SATPLAN
def satplan(problem):
    solver = Minisat22() # Crear una instancia del solucionador Minisat22
    for clause in problem:
        solver.add_clause(clause) # Agregar cl�usulas al solucionador

    # Buscar una soluci�n al problema SAT
    if solver.solve():
        solution = solver.get_model() # Obtener el modelo de la soluci�n
        return solution
    else:
        return "No hay soluci�n" # Devolver un mensaje si no se encuentra una soluci�n

# Funci�n principal
def main():
    # Definir el problema de SAT como una lista de cl�usulas
    problem = [[1, 2, -3], [-1, 2], [2, 3]]

    # Resolver el problema utilizando SATPLAN
    solution = satplan(problem)

    # Imprimir la soluci�n encontrada
    if solution != "No hay soluci�n":
        print("Soluci�n encontrada:", solution)
    else:
        print("No se encontr� una soluci�n para el problema SAT.")

if __name__ == "__main__":
    main()

