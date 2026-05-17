# 4. No Sistema Operacional Linux, o comando para realizar uma operação de ping com 10 iterações é ping -4 -c 10 <servidor> e no Sistema Operacional Windows, o comando para a mesma função é ping -4 -n 10 <servidor>. Fazer uma aplicação Java que rode 3 Threads, sendo que a Thread deve identificar o SO para rodar o comando certo, fazendo operação de ping para os servidores UOL (www.uol.com.br), Terra (www.terra.com.br) e Google (www.google.com.br). Cada thread deve ler a saída do ping imprimindo, a cada iteração, o nome do servidor (usar fixo: UOL, Terra ou Google) e o tempo daquela iteração. Ao fim, deve-se exibir o nome do servidor (usar fixo: UOL, Terra ou Google) e o tempo médio obtido pela operação. Outros Sistemas Operacionais devem ser descartados.

import multiprocessing
import platform
import subprocess
import time


def so_name():
    so: str = ""
    so = platform.system()
    return so


def ping(server_name):
    so: str = ""
    command: str = ""
    vector_command: str = []
    so = so_name()
    output: str = ""
    line: str = ""
    data: str = ""

    if server_name == "UOL":
        server = "www.uol.com.br"
    elif server_name == "Terra":
        server = "www.terra.com.br"
    elif server_name == "Google":
        server = "www.google.com.br"

    if so == "Linux":
        command = f"ping -4 -c 10 {server}"
        vector_command = command.split()
        output = subprocess.Popen(vector_command, stdout=subprocess.PIPE)
        line = output.stdout.readline().decode("utf-8", errors="ignore")

        while line:
            if "time=" in line:
                data = line.split("time=")
                data = data[1].split(" ")
                data = data[0] + "ms"
                print(f"Tempo de iteração do {server_name}: {data}")
            if "min/avg/max/mdev" in line:
                data = line.split()
                data = data[3].split("/")
                data = data[1] + "ms"
                print(f"Tempo médio de reposta do {server_name}: {data}")
            line = output.stdout.readline().decode("utf-8", errors="ignore")

    elif so == "Windows":
        command = "ping -4 -n 10 www.google.com.br"
        vector_command = command.split()
        output = subprocess.Popen(vector_command, stdout=subprocess.PIPE)
        line = output.stdout.readline().decode("utf-8", errors="ignore")

        while line:
            if ("time=" in line) and ("ms" in line):
                data = line.split("time=")
                data = data[1].split("ms")
                data = data[0] + "ms"
                print(f"Tempo de iteração do {server_name}: {data}")
            if "Média" in line:
                data = line.split("=")
                data = data[5]
                print(f"Tempo médio de reposta do {server_name}: {data}")
            line = output.stdout.readline().decode("utf-8", errors="ignore")
            time.sleep(0.1)
    else:
        print("Sistema operacional não suportado.")


def main():
    servers = ["UOL", "Terra", "Google"]

    with multiprocessing.Pool(processes=3) as pool:
        pool.map(ping, servers)


if __name__ == "__main__":
    main()
