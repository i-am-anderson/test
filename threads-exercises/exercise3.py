# 3) Fazer uma aplicação de uma corrida de sapos, com 5 Threads, cada Thread controlando 1 sapo. Deve haver um tamanho máximo para cada pulo do sapo (em centímetros) e a distância máxima para que os sapos percorram. A cada salto, um sapo pode dar um salto de 0 até o tamanho máximo do salto (valor aleatório entre 1 e 5 cm.). Após dar um salto, a Thread, para cada sapo, deve mostrar no console, qual foi o tamanho do salto e quanto o sapo percorreu. Assim que o sapo percorrer a distância máxima, a Thread deve apresentar que o sapo chegou. Dica: O exercício deve ser resolvido todo em console, ou seja, como se estivesse sendo narrado.

import multiprocessing
import random
import time


def process_thread(id):
    jump: int = 0
    min_jump: int = 1
    max_jump: int = 5
    max_distance: int = 100
    distance: int = 0

    while distance < max_distance:
        jump = random.randint(min_jump, max_jump)
        distance += jump
        time.sleep(0.1)
        print(f"Sapo {id} pulou {jump} cm. Distância percorrida: {distance} cm.")

    print(f"Sapo {id}: Chegou ao final da corrida!")


def main():
    threads: int = 5
    params: int = [0] * threads

    for i in range(threads):
        params[i] = i + 1

    with multiprocessing.Pool(processes=threads) as pool:
        pool.map(process_thread, params)


if __name__ == "__main__":
    main()
