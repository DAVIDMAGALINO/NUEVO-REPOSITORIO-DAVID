def buscar_valor(matriz, valor_busqueda):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor_busqueda:
                return f"El valor {valor_busqueda} se encontró en la posición ({i}, {j})"
    return "El valor no se encontró en la matriz"

# Definir una matriz de ejemplo
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Definir el valor a buscar
valor_busqueda = 5

# Llamar a la función de búsqueda
resultado = buscar_valor(matriz, valor_busqueda)
print(resultado)
