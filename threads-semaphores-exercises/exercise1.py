# 1. Fazer uma aplicação, console, que gerencie a figura abaixo: Para tal, usar uma variável sentido, que será alterado pela Thread que controla cada carro com a movimentação do carro. Quando a Thread tiver a possibilidade de ser executada, ela deve imprimir em console o sentido que o carro está passando. Só pode passar um carro por vez no cruzamento.

import multiprocessing
import time

sentido_shared: int = 0
sem: None


def init(val, s):
    global sentido_shared, sem
    sentido_shared = val
    sem = s


def process_thread(id):
    global sentido_shared, sem

    with sem:
        print(f"Carro {id} está passando no sentido {sentido_shared.value}")

        # Simula o tempo que o carro leva para atravessar o cruzamento
        time.sleep(2)
        print(f"Carro {id} terminou de passar no cruzamento.")

        # Simula o tempo entre os carros passando
        time.sleep(0.1)

        # Alterna o sentido para o próximo carro
        sentido_shared.value = (sentido_shared.value + 1) % 4


def main():
    threads: int = 4
    params: int = [0] * threads
    semaphore = None
    sentido: int = 0

    with multiprocessing.Manager() as manager:
        # Variável compartilhada para controlar o sentido dos carros no cruzamento
        sentido = manager.Value("i", 0)

        # Semáforo para controlar o acesso à variável compartilhada com permissão de apenas 1 thread por vez (mutex)
        semaphore = manager.Semaphore(1)

        for i in range(threads):
            params[i] = i + 1

        with multiprocessing.Pool(
            processes=threads, initializer=init, initargs=(sentido, semaphore)
        ) as pool:
            pool.map(process_thread, params)


if __name__ == "__main__":
    main()
