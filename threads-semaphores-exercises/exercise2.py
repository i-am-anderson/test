# 2. Quatro pessoas caminham, cada uma em um corredor diferente. Os 4 corredores terminam em uma única porta. Apenas 1 pessoa pode cruzar a porta, por vez. Considere que cada corredor tem 200m. e cada pessoa anda de 4 a 6 m/s. Cada pessoa leva de 1 a 2 segundos para abrir e cruzar a porta. Faça uma aplicação que simule essa situação.

import multiprocessing
import random
import time

sem: None
person: int = 0


def init(val, s):
    global person, sem
    person = val
    sem = s


def process_thread(id):
    global person, sem
    distance: int = 200

    while distance > 0:
        speed = random.randint(4, 6)  # Velocidade entre 4 e 6 m/s
        distance -= speed  # Atualiza a distância restante
        print(
            f"Pessoa {id} está caminhando. Distância restante: {max(distance, 0):.2f} m"
        )
        time.sleep(0.1)

    with sem:
        print(f"Pessoa {id} está cruzando a porta.")

        # Simula o tempo que a pessoa leva para abrir e cruzar a porta (1 a 2 segundos)
        crossing_time = random.randint(1, 2)
        time.sleep(crossing_time)

        print(f"Pessoa {id} terminou de cruzar a porta.")

    time.sleep(0.1)


def main():
    threads: int = 4
    params: int = [0] * threads
    semaphore = None
    person: int = 0

    with multiprocessing.Manager() as manager:
        # Variável compartilhada para controlar o acesso à porta
        person = manager.Value("i", 0)

        # Semáforo para controlar o acesso à variável compartilhada com permissão de apenas 1 thread por vez (mutex)
        semaphore = manager.Semaphore(1)

        for i in range(threads):
            params[i] = i + 1

        with multiprocessing.Pool(
            processes=threads, initializer=init, initargs=(person, semaphore)
        ) as pool:
            pool.map(process_thread, params)


if __name__ == "__main__":
    main()
