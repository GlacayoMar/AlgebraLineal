from fractions import Fraction


def crear_matriz_aleatoria(tamano):
    import random
    matriz = [[random.randint(1, 10) for _ in range(tamano)] for _ in range(tamano)]
    return matriz


def ingresar_matriz_usuario(tamano):
    print("Por favor, ingrese los elementos de la matriz fila por fila.")
    matriz = []
    for i in range(tamano):
        fila = list(map(int, input(
            f"Ingrese los elementos de la fila {i + 1} separados por espacio (solo números positivos): ").split()))
        if len(fila) != tamano:
            print(f"Error: La fila debe tener {tamano} elementos.")
            return None
        matriz.append(fila)
    return matriz


def imprimir_matriz(matriz):
    # Definir un ancho fijo para los elementos (ajustable según lo necesites)
    ancho = 10

    for fila in matriz:
        # Formatear cada elemento para que tenga el mismo ancho y esté centrado
        print(" ".join(f"{str(Fraction(elem).limit_denominator()):^{ancho}}" if isinstance(elem,
                                                                                           float) else f"{str(elem):^{ancho}}"
                       for elem in fila))
    print()


def escalonar_matriz(matriz, tamano):
    # Algoritmo de eliminación gaussiana
    for i in range(tamano):
        # Hacer que el pivote sea 1 (dividiendo toda la fila por el valor del pivote)
        pivote = matriz[i][i]
        if pivote == 0:
            # Encontrar una fila que tenga un valor diferente de cero en la columna actual
            for j in range(i + 1, tamano):
                if matriz[j][i] != 0:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    print(f"Intercambio: F{i + 1} <--> F{j + 1}")
                    imprimir_matriz(matriz)
                    pivote = matriz[i][i]
                    break
            else:
                print(f"La matriz es inconsistente en la fila {i + 1}.")
                return False  # No es posible convertir a una matriz identidad

        if pivote != 1:
            matriz[i] = [x / pivote for x in matriz[i]]
            print(f"F{i + 1} --> (1/{Fraction(pivote).limit_denominator()}) * F{i + 1}")
            imprimir_matriz(matriz)

        # Hacer ceros en las demás filas en la columna i
        for j in range(tamano):
            if j != i:
                factor = matriz[j][i]
                matriz[j] = [matriz[j][k] - factor * matriz[i][k] for k in range(tamano)]
                print(f"F{j + 1} --> F{j + 1} - ({Fraction(factor).limit_denominator()}) * F{i + 1}")
                imprimir_matriz(matriz)
    return True


def matriz_identidad(tamano):
    identidad = [[1 if i == j else 0 for j in range(tamano)] for i in range(tamano)]
    return identidad


def resolver_matriz():
    print("Elija una opción:")
    print("1. Crear matriz aleatoria")
    print("2. Ingresar matriz manualmente")

    opcion = int(input("Ingrese su opción: "))
    tamano = int(input("Ingrese el tamaño de la matriz cuadrada: "))

    if opcion == 1:
        matriz = crear_matriz_aleatoria(tamano)
    elif opcion == 2:
        matriz = ingresar_matriz_usuario(tamano)
        if matriz is None:
            return
    else:
        print("Opción no válida")
        return

    print("Matriz inicial:")
    imprimir_matriz(matriz)

    if escalonar_matriz(matriz, tamano):
        print("La matriz ha sido transformada a una matriz identidad:")
        identidad = matriz_identidad(tamano)
        imprimir_matriz(identidad)
    else:
        print("No se pudo resolver la matriz.")


resolver_matriz()