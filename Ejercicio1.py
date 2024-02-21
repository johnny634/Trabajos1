# array bidimensionales ejercicio 1

grefa = [
#   0,   1,   2 Columna
    [8,  6,    6], # 0 Fila

    [9,  17,   77],  # 1

    [21, 9,    54]]  # 2


def buscar(grefa, valor):
    for i in range(len(grefa)):
        for j in range(len(grefa[i])):
            if grefa[i][j] == valor:
                return f"El valor {valor} , se encontro en la posión ({i}, {j})."
    return f"El valor {valor}, no se encontro en la matriz"


# Valor a buscar

valor_a_buscar = 54

# Llamada a la función para buscar el valor
resul = buscar(grefa, valor_a_buscar)

print(resul)
