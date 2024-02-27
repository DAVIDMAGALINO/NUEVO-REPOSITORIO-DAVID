def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def ordenar_fila(matriz, fila):
    fila_a_ordenar = matriz[fila]
    bubble_sort(fila_a_ordenar)
    matriz[fila] = fila_a_ordenar

# Matriz original
matriz = [
    [3, 2, 7],
    [1, 5, 4],
    [9, 6, 8]
]

# Mostrar matriz original
print("Matriz Original:")
for row in matriz:
    print(row)

# Ordenar fila 1
ordenar_fila(matriz, 1)

# Mostrar matriz con fila ordenada
print("\nMatriz con Fila Ordenada:")
for row in matriz:
    print(row)


