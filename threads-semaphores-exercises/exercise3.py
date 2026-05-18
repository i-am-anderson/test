# 3. Fazer uma aplicação de uma corrida de sapos, com 5 Threads, cada Thread controlando 1 sapo. Deve haver um tamanho máximo para cada pulo do sapo (em centímetros) e a distância máxima para que os sapos percorram. A cada salto, um sapo pode dar um salto de 0 até o tamanho máximo do salto (valor aleatório entre 1 e 5 cm.). Após dar um salto, a Thread, para cada sapo, deve mostrar no console, qual foi o tamanho do salto e quanto o sapo percorreu. Assim que o sapo percorrer a distância máxima, a Thread deve apresentar a posição que o sapo chegou.

import multiprocessing
import random
import time

ranking_shared: int = [0] * 5
sem: None


def init(val, s):
    global ranking_shared, sem
    ranking_shared = val
    sem = s


def process_thread(id):
    global ranking_shared, sem

    jump: int = 0
    min_jump: int = 1
    max_jump: int = 5
    max_distance: int = 100
    distance: int = 0

    with sem:
        while distance < max_distance:
            jump = random.randint(min_jump, max_jump)
            distance += jump

            if distance > max_distance:
                distance = max_distance
                jump = max_distance - (distance - jump)

            time.sleep(0.1)
            print(f"Sapo {id} pulou {jump} cm. Distância percorrida: {distance} cm.")

        ranking_shared.append(id)
        print(f"Sapo {id}: Chegou ao final da corrida!")
        print(f"Sapo {id}: Posição final: {len(ranking_shared)}º lugar.")


def main():
    threads: int = 5
    qty_threads_sem: int = 5
    params: int = [0] * threads
    ranking: int = [0] * threads
    semaphore = None

    with multiprocessing.Manager() as manager:
        # Variável compartilhada para controlar a posição dos sapos na corrida
        ranking = manager.list()

        # Semáforo para controlar o acesso à variável compartilhada com permissão de apenas X (qty_threads_sem) thread(s) por vez
        semaphore = manager.Semaphore(qty_threads_sem)

        for i in range(threads):
            params[i] = i + 1

        with multiprocessing.Pool(
            processes=threads, initializer=init, initargs=(ranking, semaphore)
        ) as pool:
            pool.map(process_thread, params)

        print("\nRanking final dos sapos:")
        for i, sapo in enumerate(ranking):
            print(f"{i + 1}º lugar: Sapo {sapo}")


if __name__ == "__main__":
    main()
