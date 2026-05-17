# 2. Fazer uma aplicação que, na main, inicialize uma variável id, inteira e inicialize 5 variáveis inteiras para valores, crie um vetor de parâmetros, com o id como primeiro parâmetro e um vetor com os 5 valores recebidos. As variáveis que recebem os valores devem receber, cada uma delas, um valor aleatório de 1 a 100. Esses parâmetros devem ser preenchidos para 3 chamadas de Threads. Faça 3 chamadas de Threads, passando os parâmetros e, cada Thread, deve calcular a soma de cada linha (Cada iteração do laço, para a soma deve ser seguido por um sleep de 0.2 segundos), ao final, deve-se imprimir a identificação da linha e o resultado da soma.

import multiprocessing
import random
import time


def process_thread(id, values):
    total = 0

    for value in values:
        total += value
        time.sleep(0.2)

    print(f"Thread ID: {id} | Soma da linha: {total}")


def main():
    id: int = [0] * 5
    values: int = [0] * 5
    params: int = [(0, [0] * 5)] * 3

    for i in range(3):
        values = [0] * 5
        id[i] = i

        for j in range(5):
            values[j] = random.randint(1, 100)

        params[i] = (id[i], values)

    multiprocessing.Pool(processes=3).starmap(process_thread, params)


if __name__ == "__main__":
    main()
