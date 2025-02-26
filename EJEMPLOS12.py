# Definir una matriz 3x3 con valores numéricos
matriz = [
    [5, 8, 12],
    [3, 7, 4],
    [6, 2, 9]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición (fila, columna)
    return None  # Retorna None si no se encuentra el valor

# Solicitar un valor al usuario para buscar
valor_buscado = int(input("Introduce el valor a buscar en la matriz: "))

# Llamar a la función y mostrar el resultado
resultado = buscar_valor(matriz, valor_buscado)

if resultado:
    print(f"El valor {valor_buscado} se encontró en la posición: {resultado}")
else:
    print(f"El valor {valor_buscado} no se encuentra en la matriz.")