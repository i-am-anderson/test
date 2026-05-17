# 1. Fazer uma aplicação que rode 5 Threads que cada uma delas receba um inteiro chamado id como parâmetro e imprima no console o texto “Thread #” + id. Antes de imprimir o valor, deve- se fazer um sleep de 0.5 segundos.

import multiprocessing
import time


def process_thread(id):
    time.sleep(0.5)
    print(f"Thread #{id}")


def main():
    i: int = 5
    params: int = [0] * i

    for i in range(i):
        params[i] = i

    with multiprocessing.Pool(processes=i) as pool:
        pool.map(process_thread, params)


if __name__ == "__main__":
    main()
