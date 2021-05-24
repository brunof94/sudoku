import os


def main():
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    terminado = False
    tablero = []
    for i in range(0, 9*9):
        tablero.append("_")

    def mostrar_tablero(tablero):
        tablero_impreso = "\t1\t2\t3\t4\t5\t6\t7\t8\t9\n\n\n1\t"
        aux = 2
        for indice in range(len(tablero)):
            tablero_impreso += f'{str(tablero[indice])}\t'
            if indice % 9 == 8:
                if aux < 10:
                    tablero_impreso += f'\n\n{aux}\t'
                    aux += 1
        print(tablero_impreso)

    def cambiar_numero(x, y, valor):
        numero = (y - 1) * 9 + x - 1
        tablero[numero] = valor

    def check_tablero(tablero):
        return terminado


    mostrar_tablero(tablero)

    while True:
        clear_console()
        mostrar_tablero(tablero)
        try:
            print("-------------------------------------------------------------------------")
            pos_x = int(input("Escriba la coordenada horizontal: "))
            pos_y = int(input("Escriba la coordenada vertical: "))
            valor_nuevo = int(input("Escriba el nuevo valor: "))
            if pos_x > 9 or pos_x < 1 or pos_y > 9 or pos_y < 1:
                print("Las coordenadas deben estar entre 1 y 9")
                break
            if 0 > valor_nuevo > 10:
                print("El valor debe estar ")
            cambiar_numero(pos_x, pos_y, valor_nuevo)
        except ValueError:
            print("No se ingresaron numeros")
        check_tablero(tablero)
        if terminado:
            clear_console()
            mostrar_tablero()


if __name__ == "__main__":
    main()
