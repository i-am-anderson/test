# 31. Calcule e mostre o quadrado dos números entre 10 e 150.
import os

dir: str = ""
arq: str = ""


# Procedimento de gravação em arquivo
def grava(cont, initial, rslt):
    global dir
    global arq

    dir = "/tmp/exercicios"
    arq = "ex31.txt"

    file: str = ""
    tipo: str = ""
    enc: str = ""
    linha: str = ""

    if os.path.exists(dir) and os.path.isdir(dir):
        tipo = "w"
        enc = "utf-8"
        linha = str(rslt) + "\n"
        file = os.path.join(dir, arq)

        if os.path.exists(file) and os.path.isfile(file) and (cont > initial):
            tipo = "a"

        with open(file, tipo, encoding=enc) as fl:
            fl.write(linha)
    else:
        print("Diretório não existe!")


# Função que faz o somatório e imprime em tela
def calc(ini, fin):
    sum_: float = 0.0

    for n in range(ini, fin + 1, 1):
        grava(n, ini, f"{n}²={n**2}")
        print(f"{n}²={n**2}", end=" -> ")

    return sum_


def main():
    result: int = 0

    # cria o diretório e dá as permissões necessárias
    os.makedirs("/tmp/exercicios", exist_ok=True)
    os.chmod("/tmp/exercicios", 0o744)

    result = calc(10, 150)

    print(f"{result:,.2f}")


if __name__ == "__main__":
    main()
