def sort_row(matrix, row_index):
    if row_index < 0 or row_index >= len(matrix):
        print("Índice de fila fuera de rango")
        return

    matrix[row_index] = sorted(matrix[row_index])

# Ejemplo de uso
matrix = [
    [3, 7, 2, 8],
    [5, 1, 4, 6],
    [9, 0, 3, 2]
]
row_index = 1  # Ordenar la segunda fila (índice 1)

print("Matriz antes de ordenar:")
for row in matrix:
    print(row)

sort_row(matrix, row_index)

print("\nMatriz después de ordenar la fila", row_index, "en orden ascendente:")
for row in matrix:
    print(row)



