import ast

transpuesta = lambda matriz: list(map(lambda *columna: list(columna), *matriz)) if matriz else []
es_matriz = lambda matriz: isinstance(matriz, list) and all(map(lambda fila: isinstance(fila, list), matriz))
es_regular = lambda matriz: len(set(map(lambda fila: len(fila), matriz))) <= 1


def procesar(matriz):
    print("Entrada:", matriz)
    if not es_matriz(matriz):
        print("La entrada debe ser una lista de listas.")
        return
    if not es_regular(matriz):
        print("Todas las filas deben tener la misma longitud.")
        return
    if not matriz:
        print("La matriz está vacía.")
    print("Salida:", transpuesta(matriz))


def main():
    print("Ejemplo del enunciado")
    procesar([[1, 2, 3, 1], [4, 5, 6, 0], [7, 8, 9, -1]])
    while True:
        print()
        try:
            texto = input("Ingrese una matriz como lista de listas (Enter para salir): ").strip()
            if not texto:
                break
            matriz = ast.literal_eval(texto)
        except EOFError:
            break
        except (ValueError, SyntaxError):
            print("Entrada inválida.")
            continue
        procesar(matriz)


if __name__ == "__main__":
    main()
