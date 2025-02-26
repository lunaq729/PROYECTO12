# Definición de la matriz bidimensional
matriz = [
    [5, 2, 9],
    [1, 4, 7],
    [6, 8, 3]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición (fila, columna)
    return None  # Si no se encuentra el valor

# Función para ordenar una fila de la matriz con Bubble Sort
def ordenar_fila_bubble(matriz, fila):
    # Aplicamos el algoritmo de Bubble Sort a la fila indicada
    for i in range(len(matriz[fila]) - 1):
        for j in range(len(matriz[fila]) - 1 - i):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambiamos los valores
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Buscar un valor en la matriz
valor_buscar = 7
resultado_busqueda = buscar_valor(matriz, valor_buscar)

if resultado_busqueda:
    print(f"\nEl valor {valor_buscar} se encontró en la posición {resultado_busqueda}.")
else:
    print(f"\nEl valor {valor_buscar} no se encontró en la matriz.")

# Ordenar una fila específica (por ejemplo, la fila 1)
fila_a_ordenar = 1
ordenar_fila_bubble(matriz, fila_a_ordenar)

# Mostrar la matriz después de ordenar la fila
print(f"\nMatriz después de ordenar la fila {fila_a_ordenar}:")
for fila in matriz:
    print(fila)