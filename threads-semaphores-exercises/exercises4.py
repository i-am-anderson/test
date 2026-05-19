# 4. Você foi contratado para automatizar um treino de Fórmula 1. As regras estabelecidas pela direção da prova são simples: “No máximo 5 carros das 7 escuderias(equipes) (Cada escuderia tem 2 carros diferentes, portanto, 14 carros no total) presentes podem entrar na pista simultaneamente, mas apenas um carro de cada equipe. O segundo carro deve ficar à espera, caso um companheiro de equipe já esteja na pista. Cada piloto deve dar 3 voltas na pista. O tempo de cada volta deverá ser exibido.

import multiprocessing
import random
import time

shared_running_cars = None
shared_running_teams = None
sem_1 = None  # 5
sem_2 = None  # 2


def init(current_cars, current_teams, s1, s2):
    global shared_running_cars, shared_running_teams, sem_1, sem_2

    shared_running_cars = current_cars
    shared_running_teams = current_teams
    sem_1 = s1
    sem_2 = s2


def process_thread(team_id, car_id):
    global shared_running_cars, shared_running_teams, sem_1, sem_2

    total_laps: int = 3
    partial_time: float = 0.0
    total_time: float = 0.0

    # 1. Garante que dois carros da MESMA equipe não tentem entrar na pista ao mesmo tempo
    with sem_2[team_id]:

        # 2. Garante que a pista respeite o limite máximo de 5 carros no total
        with sem_1:
            shared_running_teams[team_id] = 1
            shared_running_cars.value += 1

            print(
                f"Equipe {team_id} - Carro {car_id} ENTROU NA PISTA! (Total na pista: {shared_running_cars.value})"
            )

            for lap in range(1, total_laps + 1):
                partial_time = round(random.uniform(1.0, 2.0), 3)
                time.sleep(partial_time)
                total_time += partial_time
                print(
                    f"Equipe {team_id} - Carro {car_id} | Volta {lap}/3: {partial_time}s"
                )

            shared_running_cars.value -= 1
            shared_running_teams[team_id] = 0

            print(
                f"Equipe {team_id} - Carro {car_id} SAIU DA PISTA! Tempo Total: {round(total_time, 3)}s"
            )


def main():
    threads: int = 14
    running_cars: int = 0
    params: int = []
    running_teams: int = []
    semaphore: None
    semaphore_2: None = []

    for team in range(7):
        for car in range(2):
            params.append((team + 1, car + 1))

    with multiprocessing.Manager() as manager:
        running_cars = manager.Value("i", 0)
        running_teams = manager.Array("i", [0] * 8)

        semaphore = manager.Semaphore(5)
        for _ in range(8):
            semaphore_2.append(manager.Semaphore(1))

        with multiprocessing.Pool(
            processes=threads,
            initializer=init,
            initargs=(running_cars, running_teams, semaphore, semaphore_2),
        ) as pool:
            pool.starmap(process_thread, params)


if __name__ == "__main__":
    main()
