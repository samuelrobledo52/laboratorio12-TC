import ast

potencia = lambda lista, n: list(map(lambda x: x ** n, lista))
es_numero = lambda x: isinstance(x, (int, float)) and not isinstance(x, bool)
son_numeros = lambda lista: isinstance(lista, list) and all(map(es_numero, lista))
es_entero_positivo = lambda n: isinstance(n, int) and not isinstance(n, bool) and n > 0


def procesar(lista, n):
    print("Entrada:", lista)
    print("n:", n)
    if not son_numeros(lista):
        print("La entrada debe ser una lista de números.")
        return
    if not es_entero_positivo(n):
        print("n debe ser un entero positivo.")
        return
    print("Salida:", potencia(lista, n))


def main():
    print("Ejemplo del enunciado")
    procesar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
    while True:
        print()
        try:
            texto = input("Ingrese una lista de números (Enter para salir): ").strip()
            if not texto:
                break
            lista = ast.literal_eval(texto)
            n = ast.literal_eval(input("Ingrese n: ").strip())
        except EOFError:
            break
        except (ValueError, SyntaxError):
            print("Entrada inválida.")
            continue
        procesar(lista, n)


if __name__ == "__main__":
    main()
