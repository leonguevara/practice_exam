# En caso de que necesites importar bibliotecas, éste es el lugar correcto para
# hacerlo.


def genera_palabra(subcadena):
    nueva_cadena = ''
    for c in subcadena:
        nueva_cadena += c * (ord(c) - 96)
    return nueva_cadena
    pass


# Esta es la función principal de tu programa.  En caso de que necesites crear más
# funciones, escríbelas antes de esta función.
def main():
    # Escribe tu código bajo esta línea, en sustitución de pass
    resultados = []
    Q = int(input())
    cancion = input()
    for q in range(Q):
        i, d = map(int, input().split())
        resultados.append(genera_palabra(cancion[i-1:d]))
    for resultado in resultados:
        print(len(resultado))
    pass


if __name__ == '__main__':
    main()
