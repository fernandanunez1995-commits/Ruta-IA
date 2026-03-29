# ==========================================
# SISTEMA INTELIGENTE DE RUTAS CON A*
# ==========================================

import heapq
import math

# -------------------------------
# 1. BASE DE CONOCIMIENTO
# -------------------------------
# Grafo (conexiones)

transporte = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3, 'F': 6},
    'C': {'A': 10, 'D': 1, 'F': 4},
    'D': {'B': 3, 'C': 1, 'E': 2},
    'E': {'D': 2, 'A': 15},
    'F': {'C': 4, 'B': 6}
}

# Coordenadas (para heurística)
# Simula posiciones reales (ej: estaciones)
coordenadas = {
    'A': (0, 0),
    'B': (2, 2),
    'C': (1, 5),
    'D': (5, 3),
    'E': (7, 5),
    'F': (4, 2)
}


# -------------------------------
# 2. HEURÍSTICA (distancia euclidiana)
# -------------------------------
def heuristica(nodo, objetivo):
    x1, y1 = coordenadas[nodo]
    x2, y2 = coordenadas[objetivo]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# -------------------------------
# 3. ALGORITMO A*
# -------------------------------
def a_estrella(grafo, inicio, fin):
    cola = [(0, inicio, [])]  # (f, nodo, ruta)
    costos = {inicio: 0}

    while cola:
        (f, nodo, ruta) = heapq.heappop(cola)

        ruta = ruta + [nodo]

        if nodo == fin:
            return costos[nodo], ruta

        for vecino, peso in grafo[nodo].items():
            nuevo_costo = costos[nodo] + peso

            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica(vecino, fin)
                heapq.heappush(cola, (prioridad, vecino, ruta))

    return float("inf"), []

# -------------------------------
# 4. INTERACCIÓN CON EL USUARIO
# -------------------------------
print("=== SISTEMA INTELIGENTE DE RUTAS (A*) ===")

inicio = input(" Por favor ingrese el punto de inicio (A, B, C, D, E,F): ").upper()
fin = input(" Por favor ingrese el punto de destino (A, B, C, D, E, f): ").upper()

if inicio not in transporte or fin not in transporte:
    print("Error: Nodo inválido")
else:
    costo, ruta = a_estrella(transporte, inicio, fin)

    print("\n--- RESULTADO ---")
    print("Ruta más óptima:", " -> ".join(ruta))
    print("Costo total:", costo)