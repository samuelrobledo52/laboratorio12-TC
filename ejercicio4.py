import ast

eliminar = lambda lista, quitar: list(filter(lambda x: x not in quitar, lista))
son_listas = lambda *listas: all(map(lambda l: isinstance(l, list), listas))


def procesar(lista, quitar):
    print("Entrada:", lista)
    print("Elementos a eliminar:", quitar)
    if not son_listas(lista, quitar):
        print("Ambas entradas deben ser listas.")
        return
    if not lista:
        print("La lista está vacía.")
    print("Salida:", eliminar(lista, quitar))


def main():
    colores = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
    quitar = ['amarillo', 'café', 'blanco']
    print("Ejemplo del enunciado")
    procesar(colores, quitar)
    while True:
        print()
        try:
            texto = input("Ingrese la lista original (Enter para salir): ").strip()
            if not texto:
                break
            lista = ast.literal_eval(texto)
            quitar = ast.literal_eval(input("Ingrese la lista de elementos a eliminar: ").strip())
        except EOFError:
            break
        except (ValueError, SyntaxError):
            print("Entrada inválida.")
            continue
        procesar(lista, quitar)


if __name__ == "__main__":
    main()
