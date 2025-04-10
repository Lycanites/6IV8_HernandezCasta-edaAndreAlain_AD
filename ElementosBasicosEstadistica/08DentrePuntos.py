import itertools
import math

# Puntos en el plano
puntos = {
    "A": (2, 3),
    "B": (5, 4),
    "C": (1, 1),
    "D": (6, 7),
    "E": (3, 5),
    "F": (8, 2),
    "G": (4, 6),
    "H": (2, 1),
}

# Funciones de distancia
def euclidiana(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def manhattan(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def chebyshev(p1, p2):
    return max(abs(p2[0] - p1[0]), abs(p2[1] - p1[1]))

# Calcular distancias para todos los pares
distancias = []
for (p1, coord1), (p2, coord2) in itertools.combinations(puntos.items(), 2):
    distancias.append({
        "par": (p1, p2),
        "euclidiana": euclidiana(coord1, coord2),
        "manhattan": manhattan(coord1, coord2),
        "chebyshev": chebyshev(coord1, coord2)
    })

# Encontrar los extremos
def extremos_por_distancia(distancias, tipo):
    min_par = min(distancias, key=lambda x: x[tipo])
    max_par = max(distancias, key=lambda x: x[tipo])
    return min_par, max_par

# Resultados
euclid_extremos = extremos_por_distancia(distancias, "euclidiana")
manhattan_extremos = extremos_por_distancia(distancias, "manhattan")
chebyshev_extremos = extremos_por_distancia(distancias, "chebyshev")

print("=== Distancia Euclidiana ===")
print("Más cercano:", euclid_extremos[0])
print("Más lejano:", euclid_extremos[1])

print("\n=== Distancia Manhattan ===")
print("Más cercano:", manhattan_extremos[0])
print("Más lejano:", manhattan_extremos[1])

print("\n=== Distancia Chebyshev ===")
print("Más cercano:", chebyshev_extremos[0])
print("Más lejano:", chebyshev_extremos[1])
