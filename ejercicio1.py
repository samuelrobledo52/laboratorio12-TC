import ast

ordenar = lambda lista, clave: sorted(lista, key=lambda d: d[clave])
son_diccionarios = lambda lista: isinstance(lista, list) and all(map(lambda d: isinstance(d, dict), lista))
tiene_clave = lambda lista, clave: all(map(lambda d: clave in d, lista))


def procesar(lista, clave):
    print("Entrada:", lista)
    print("Key:", clave)
    if not son_diccionarios(lista):
        print("La entrada debe ser una lista de diccionarios.")
        return
    if not tiene_clave(lista, clave):
        print(f"La key '{clave}' no existe en todos los diccionarios.")
        return
    try:
        resultado = ordenar(lista, clave)
    except TypeError:
        print(f"Los valores de la key '{clave}' no se pueden comparar entre sí.")
        return
    print("Salida:", resultado)


def main():
    ejemplo = [
        {'make': 'Nokia', 'model': 216, 'color': 'Black'},
        {'make': 'Apple', 'model': 2, 'color': 'Silver'},
        {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
        {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
    ]
    print("Ejemplo del enunciado")
    procesar(ejemplo, 'model')
    while True:
        print()
        try:
            texto = input("Ingrese una lista de diccionarios (Enter para salir): ").strip()
            if not texto:
                break
            lista = ast.literal_eval(texto)
            clave = input("Ingrese la key: ").strip()
        except EOFError:
            break
        except (ValueError, SyntaxError):
            print("Entrada inválida.")
            continue
        procesar(lista, clave)


if __name__ == "__main__":
    main()
