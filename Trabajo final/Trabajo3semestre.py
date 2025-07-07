import random
import time

# Función para la búsqueda secuencial
def busqueda_secuencial(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i  # Retorna el índice del objetivo
    return -1  # Retorna -1 si no encuentra el objetivo

# Función para el algoritmo Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    # Recorremos todo el arreglo
    for i in range(n):
        # Últimos i elementos ya están ordenados
        for j in range(0, n-i-1):
            # Si el elemento actual es mayor que el siguiente, intercambiamos
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Función para evaluar el rendimiento de ambos algoritmos
def evaluar_algoritmos(tamaños):
    # Listas para guardar los tiempos de ejecución
    tiempos_busqueda = []
    tiempos_ordenamiento = []

    # Iterar sobre diferentes tamaños de arreglos
    for tam in tamaños:
        print(f"\nEvaluando arreglo de tamaño {tam}...")

        # Generar un arreglo de tamaño 'tam' con números aleatorios
        arr = [random.randint(1, 10000) for _ in range(tam)]
        arr_ordenado = sorted(arr)  # Ordenamos para la búsqueda secuencial

        # Elemento objetivo a buscar (un valor aleatorio dentro del arreglo)
        objetivo = random.choice(arr_ordenado)

        # Medir tiempo de la búsqueda secuencial
        inicio_busqueda = time.time()
        busqueda_secuencial(arr_ordenado, objetivo)
        fin_busqueda = time.time()
        tiempo_busqueda = fin_busqueda - inicio_busqueda
        tiempos_busqueda.append(tiempo_busqueda)

        # Medir el tiempo para el algoritmo Bubble Sort
        arr_copy = arr.copy()
        inicio_ordenamiento = time.time()
        bubble_sort(arr_copy)
        fin_ordenamiento = time.time()
        tiempo_ordenamiento = fin_ordenamiento - inicio_ordenamiento
        tiempos_ordenamiento.append(tiempo_ordenamiento)

    return tiempos_busqueda, tiempos_ordenamiento

# Función para graficar los resultados de manera ASCII
def graficar_resultados(tamaños, tiempos_busqueda, tiempos_ordenamiento):
    print("\nGráfica de resultados (Representación ASCII):")
    max_tiempo = max(max(tiempos_busqueda), max(tiempos_ordenamiento))
   
    # Factor de escala para ajustar la longitud de las barras
    escala = 50 / max_tiempo  # 50 es el largo máximo de la barra

    # Mostrar los resultados en barras ASCII
    for i in range(len(tamaños)):
        print(f"Tamaño: {tamaños[i]}")
        barra_busqueda = "|" + "-" * int(tiempos_busqueda[i] * escala) + ">"
        barra_ordenamiento = "|" + "/" * int(tiempos_ordenamiento[i] * escala) + ">"
        print(f"  Búsqueda Secuencial: {barra_busqueda} ({tiempos_busqueda[i]:.6f}s)")
        print(f"  Bubble Sort:         {barra_ordenamiento} ({tiempos_ordenamiento[i]:.6f}s)\n")

def main():
    # Definir tamaños de arreglos a probar
    tamaños = [100, 500, 1000, 5000, 10000]
   
    # Evaluar los algoritmos
    tiempos_busqueda, tiempos_ordenamiento = evaluar_algoritmos(tamaños)
   
    # Graficar los resultados usando ASCII
    graficar_resultados(tamaños, tiempos_busqueda, tiempos_ordenamiento)

if __name__ == "__main__":
    main()