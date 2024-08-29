def imprimirMatriz(matriz):
    for fila in matriz:
        print(" ".join(f"{x:.2f}" for x in fila))

def intercambioFilas(matriz, fila1, fila2):
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]

def multiplicarFila(matriz, fila, factor):
    matriz[fila] = [elemento * factor for elemento in matriz[fila]]

def sumarFilas(matriz, filaDestino, filaOrigen, factor):
    matriz[filaDestino] = [destino + factor * origen for destino, origen in zip(matriz[filaDestino], matriz[filaOrigen])]

def eliminarGaussJordan(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        # Buscar el mayor en la columna i para pivotear
        maxFila = i
        for k in range(i + 1, filas):
            if abs(matriz[k][i]) > abs(matriz[maxFila][i]):
                maxFila = k

        # Intercambiar la fila actual con la fila de mayor valor
        intercambioFilas(matriz, i, maxFila)

        # Hacer el elemento diagonal 1
        factor = matriz[i][i]
        if factor != 0:
            multiplicarFila(matriz, i, 1.0 / factor)

        # Hacer 0 los elementos por encima y por debajo del pivote
        for k in range(filas):
            if k != i and matriz[k][i] != 0:
                factor = -matriz[k][i]
                sumarFilas(matriz, k, i, factor)

def resolverMatriz(matriz):
    print("Matriz original:")
    imprimirMatriz(matriz)
    eliminarGaussJordan(matriz)
    print("Matriz convertida en identidad:")
    imprimirMatriz(matriz)

def ingresarMatriz(filas, columnas):
    matriz = []
    print(f"Ingrese los elementos de la matriz {filas}x{columnas}:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Ingrese el elemento [{i+1},{j+1}]: "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz

def main():
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))

    if filas != columnas:
        print("La matriz debe ser cuadrada para convertirla en una matriz identidad.")
        return

    matriz = ingresarMatriz(filas, columnas)
    resolverMatriz(matriz)

if __name__ == "__main__":
    main()
