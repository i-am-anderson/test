# 38.
import os

dir: str = ""
arq: str = ""


# Função
def numero_impar(num):
    if num % 2 != 0:
        return num
    else:
        return -1


# Procedimento
def ler():
    global dir
    global arq

    dir = "/tmp/exercicios"
    arq = "ex37a.txt"

    file: str = ""

    if os.path.exists(dir) and os.path.isdir(dir):
        file = os.path.join(dir, arq)

        if os.path.exists(file) and os.path.isfile(file):
            tipo = "r"
            enc = "utf-8"
            with open(file, tipo, encoding=enc) as fl:
                for _, line in enumerate(fl.readlines()):
                    num_eh_impar: int = 0

                    num_eh_impar = numero_impar(int(line))

                    if num_eh_impar != -1:
                        print(num_eh_impar)
        else:
            print("Arquivo não existe!")
    else:
        print("Diretório não existe!")


def main():
    # cria o diretório e dá as permissões necessárias
    os.makedirs("/tmp/exercicios", exist_ok=True)
    os.chmod("/tmp/exercicios", 0o744)

    ler()


if __name__ == "__main__":
    main()
