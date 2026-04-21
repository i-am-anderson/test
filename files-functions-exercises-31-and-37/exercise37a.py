# 37. Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.
import os

dir: str = ""
arq: str = ""


# Procedimento
def grava(cont, rslt):
    global dir
    global arq

    dir = "/tmp/exercicios"
    arq = "ex37a.txt"

    file: str = ""
    tipo: str = ""
    enc: str = ""
    linha: str = ""

    if os.path.exists(dir) and os.path.isdir(dir):
        tipo = "w"
        enc = "utf-8"
        linha = str(rslt) + "\n"
        file = os.path.join(dir, arq)

        if os.path.exists(file) and os.path.isfile(file) and (cont > 0):
            tipo = "a"

        with open(file, tipo, encoding=enc) as fl:
            fl.write(linha)
    else:
        print("Diretório não existe!")


def main():
    x: int = 0
    y: int = 1
    curr: int = 0
    n: int = 0

    # cria o diretório e dá as permissões necessárias
    os.makedirs("/tmp/exercicios", exist_ok=True)
    os.chmod("/tmp/exercicios", 0o744)

    while n <= 0:
        n = int(input("Digite um número inteiro: "))

    for n in range(n):
        if x == 0:
            x = 1
        else:
            y = curr
            curr = x + y
            x = y

        grava(n, curr)
        print(curr, end=", ")


if __name__ == "__main__":
    main()
