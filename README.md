# 🚍 Sistema Inteligente de Rutas con A*

## 📌 Descripción
Este proyecto implementa un sistema inteligente basado en técnicas de Inteligencia Artificial para encontrar la mejor ruta entre dos puntos dentro de un sistema de transporte.

El sistema utiliza:
- Representación del conocimiento mediante grafos
- Sistemas basados en reglas
- Algoritmo de búsqueda heurística A* (A estrella)

---

## 🧠 ¿Cómo funciona?

El sistema modela el transporte como un grafo donde:
- Cada nodo representa una estación
- Cada arista representa una conexión con un costo (distancia o tiempo)

Se aplica el algoritmo A*, que combina:
- **Costo real (g)**: distancia recorrida
- **Heurística (h)**: estimación de distancia al destino

Fórmula utilizada:

f(n) = g(n) + h(n)

Esto permite encontrar la ruta más óptima de manera eficiente.

---

## ⚙️ Tecnologías utilizadas

- Python
- Librerías estándar:
  - heapq
  - math

---

## 📂 Estructura del proyecto


Ruta-IA/
│── main.py
│── README.md


---

## ▶️ Ejecución del proyecto

1. Tener Python instalado
2. Abrir una terminal en la carpeta del proyecto
3. Ejecutar:


python main.py


4. Ingresar:
- Punto de inicio
- Punto de destino

---

## 🧪 Ejemplo de uso

Entrada:


Inicio: A
Destino: E


Salida:


Ruta más óptima: A -> B -> D -> E
Costo total: 10
